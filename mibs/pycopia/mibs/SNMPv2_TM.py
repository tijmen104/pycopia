# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_IDENTITY, snmpModules, snmpDomains, snmpProxys
from SNMPv2_TC import TEXTUAL_CONVENTION

class SNMPv2_TM(ModuleObject):
	path = '/usr/share/mibs/ietf/SNMPv2-TM'
	conformance = 5
	name = 'SNMPv2-TM'
	language = 2
	description = 'The MIB module for SNMP transport mappings.\n\nCopyright (C) The Internet Society (2002). This\nversion of this MIB module is part of RFC 3417;\nsee the RFC itself for full legal notices.'

# nodes
class snmpUDPDomain(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 1, 1])
	name = 'snmpUDPDomain'

class snmpCLNSDomain(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 1, 2])
	name = 'snmpCLNSDomain'

class snmpCONSDomain(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 1, 3])
	name = 'snmpCONSDomain'

class snmpDDPDomain(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 1, 4])
	name = 'snmpDDPDomain'

class snmpIPXDomain(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 1, 5])
	name = 'snmpIPXDomain'

class rfc1157Proxy(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 2, 1])
	name = 'rfc1157Proxy'

class rfc1157Domain(NodeObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 2, 1, 1])
	name = 'rfc1157Domain'

class snmpv2tm(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 19])
	name = 'snmpv2tm'


# macros
# types 

class SnmpUDPAddress(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(6, 6))
	format = '1d.1d.1d.1d/2d'


class SnmpOSIAddress(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(1, 1), Range(4, 85))
	format = '*1x:/1x:'


class SnmpNBPAddress(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(3, 99))


class SnmpIPXAddress(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(12, 12))
	format = '4x.1x:1x:1x:1x:1x:1x.2d'

# scalars 
# columns
# rows 
# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
