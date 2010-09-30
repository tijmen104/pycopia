#!/usr/bin/python2.4
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
# 
#    Copyright (C) 2009 Keith Dart <keith@kdart.com>
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.

"""
Generic ethernet bridge or switch.

"""
import sys

from pycopia.mibs import SNMPv2_MIB
from pycopia.SNMP import Manager


MIBNAMES = [
 "BRIDGE_MIB",
 "ENTITY_MIB",
 "EtherLike_MIB",
 "IANA_RTPROTO_MIB",
 "IANAifType_MIB",
 "IF_MIB",
 "MAU_MIB",
 "P_BRIDGE_MIB",
 "Q_BRIDGE_MIB",
 "RFC1213_MIB",
 "RMON_MIB",
 "RMON2_MIB",
 "SNMP_NOTIFICATION_MIB",
 "SNMP_TARGET_MIB",
]
MIBS = map(lambda n: __import__("pycopia.mibs.%s" % n, globals(), locals(), ["*"]), MIBNAMES)

TAGGED = "T"
UNTAGGED = "U"
UNASSIGNED = " "


class VlanTable(object):
    def __init__(self, manager=None):
        if manager is not None:
            self.update(manager)
        else:
            self.clear()

    def clear(self):
        self._maxif = 0
        self._vlanlist = []

    def __str__(self):
        blk1 = "|                  %d"
        blk2 = "|1|2|3|4|5|6|7|8|9|0"
        s =     ["PORT:" + "".join([blk1 % x for x in range(1, self._maxif / 10)])]
        s.append("VLAN " + blk2 * (self._maxif / 10))
        for vle in self._vlanlist:
            s.append(str(vle))
        return "\n".join(s)

    def __getitem__(self, idx):
        return self._vlanlist[idx]

    def update(self, manager):
        self._maxif = manager.ifNumber
        self._vlanlist = []
        vlanlist = manager.getall("dot1qVlanCurrent").values()
        for vlan in vlanlist:
            self._vlanlist.append(VlanTableEntry(vlan, self._maxif))
        self._vlanlist.sort(key=lambda o: o.vlanid)


class VlanTableEntry(object):
    def __init__(self, vlan, maxif):
        self.vlanid = vlan.dot1qVlanFdbId
        self._portlist = get_vlan_ports(vlan, maxif)

    def __str__(self):
        portmap = "|".join(self._portlist)
        return "%4.4d |%s" % (self.vlanid, portmap)

    def __cmp__(self, other):
        return cmp(self.vlanid, other.vlanid)

    def __getitem__(self, idx):
        return self._portlist[idx - 1] # SNMP sequences start at 1


def get_vlan_ports(vlan, maxif):
    ports = []
    for n, octet in enumerate(vlan.dot1qVlanCurrentEgressPorts):
        if n * 9 > maxif:
            break
        oports = [UNASSIGNED] * 8
        octet = ord(octet)
        for bit in range(8):
            if (octet << bit) & 0x80:
                oports[bit] = TAGGED
        ports.extend(oports)
    for n, octet in enumerate(vlan.dot1qVlanCurrentUntaggedPorts):
        if n * 9 > maxif:
            break
        octet = ord(octet)
        for bit in range(8):
            portnum = n * 8 + bit
            if (octet << bit) & 0x80 and ports[portnum] == TAGGED:
                ports[portnum] = UNTAGGED
    return ports



class BridgeManager(Manager.Manager):

    def get_vlan_table(self):
        return VlanTable(self)


def get_manager(device, community):
    return Manager.get_manager(device, community, BridgeManager, MIBS)


