class ClientInfoFlags:
    """
    Flags for the RDPClientInfoPDU flags field
    """
    INFO_MOUSE = 0x00000001
    INFO_DISABLECTRLALTDEL = 0x00000002
    INFO_AUTOLOGON = 0x00000008
    INFO_UNICODE = 0x00000010
    INFO_MAXIMIZESHELL = 0x00000020
    INFO_LOGONNOTIFY = 0x00000040
    INFO_COMPRESSION = 0x00000080
    INFO_ENABLEWINDOWSKEY = 0x00000100
    INFO_REMOTECONSOLEAUDIO = 0x00002000
    INFO_FORCE_ENCRYPTED_CS_PDU = 0x00004000
    INFO_RAIL = 0x00008000
    INFO_LOGONERRORS = 0x00010000
    INFO_MOUSE_HAS_WHEEL = 0x00020000
    INFO_PASSWORD_IS_SC_PIN = 0x00040000
    INFO_NOAUDIOPLAYBACK = 0x00080000
    INFO_USING_SAVED_CREDS = 0x00100000
    INFO_AUDIOCAPTURE = 0x00200000
    INFO_VIDEO_DISABLE = 0x00400000
    INFO_CompressionTypeMask = 0x00001E00


class RDPSecurityFlags:
    SEC_EXCHANGE_PKT = 0x0001
    SEC_TRANSPORT_REQ = 0x0002
    SEC_TRANSPORT_RSP = 0x0004
    SEC_ENCRYPT = 0x0008
    SEC_RESET_SEQNO = 0x0010
    SEC_IGNORE_SEQNO = 0x0020
    SEC_INFO_PKT = 0x0040
    SEC_LICENSE_PKT = 0x0080
    SEC_LICENSE_ENCRYPT_CS = 0x0100
    SEC_LICENSE_ENCRYPT_SC = 0x0200
    SEC_REDIRECTION_PKT = 0x0400
    SEC_SECURE_CHECKSUM = 0x0800
    SEC_AUTODETECT_REQ = 0x1000
    SEC_AUTODETECT_RSP = 0x2000
    SEC_HEARTBEAT = 0x4000
    SEC_FLAGSHI_VALID = 0x8000


class RDPSecurityHeaderType:
    NONE = 0
    BASIC = 1
    SIGNED = 2
    FIPS = 3


class FIPSVersion:
    TSFIPS_VERSION1 = 1


class RDPLicensingPDUType:
    LICENSE_REQUEST = 0x01
    PLATFORM_CHALLENGE = 0x02
    NEW_LICENSE = 0x03
    UPGRADE_LICENSE = 0x04
    LICENSE_INFO = 0x12
    NEW_LICENSE_REQUEST = 0x13
    PLATFORM_CHALLENGE_RESPONSE = 0x15
    ERROR_ALERT = 0xFF


class RDPLicenseBinaryBlobType:
    """
    License blob data type
    See http://msdn.microsoft.com/en-us/library/cc240481.aspx
    """
    BB_ANY_BLOB = 0x0000
    BB_DATA_BLOB = 0x0001
    BB_RANDOM_BLOB = 0x0002
    BB_CERTIFICATE_BLOB = 0x0003
    BB_ERROR_BLOB = 0x0004
    BB_ENCRYPTED_DATA_BLOB = 0x0009
    BB_KEY_EXCHG_ALG_BLOB = 0x000D
    BB_SCOPE_BLOB = 0x000E
    BB_CLIENT_USER_NAME_BLOB = 0x000F
    BB_CLIENT_MACHINE_NAME_BLOB = 0x0010


class RDPLicenseErrorCode:
    """
    @summary: License error message code
    @see: http://msdn.microsoft.com/en-us/library/cc240482.aspx
    """
    ERR_INVALID_SERVER_CERTIFICATE = 0x00000001
    ERR_NO_LICENSE = 0x00000002
    ERR_INVALID_SCOPE = 0x00000004
    ERR_NO_LICENSE_SERVER = 0x00000006
    STATUS_VALID_CLIENT = 0x00000007
    ERR_INVALID_CLIENT = 0x00000008
    ERR_INVALID_PRODUCTID = 0x0000000B
    ERR_INVALID_MESSAGE_LEN = 0x0000000C
    ERR_INVALID_MAC = 0x00000003


class RDPStateTransition:
    """
    Automata state transition
    See http://msdn.microsoft.com/en-us/library/cc240482.aspx
    """
    ST_TOTAL_ABORT = 0x00000001
    ST_NO_TRANSITION = 0x00000002
    ST_RESET_PHASE_TO_START = 0x00000003
    ST_RESEND_LAST_MESSAGE = 0x00000004


class RDPDataPDUType:
    """
    Data PDU types
    @see: http://msdn.microsoft.com/en-us/library/cc240576.aspx
    """
    PDUTYPE_DEMANDACTIVEPDU = 0x1
    PDUTYPE_CONFIRMACTIVEPDU = 0x3
    PDUTYPE_DEACTIVATEALLPDU = 0x6
    PDUTYPE_DATAPDU = 0x7
    PDUTYPE_SERVER_REDIR_PKT = 0xA


class RDPConnectionDataType:
    SERVER_CORE = 0x0C01
    SERVER_SECURITY = 0x0C02
    SERVER_NETWORK = 0x0C03
    CLIENT_CORE = 0xC001
    CLIENT_SECURITY = 0xC002
    CLIENT_NETWORK = 0xC003
    CLIENT_CLUSTER = 0xC004
    CLIENT_MONITOR = 0xC005


class RDPVersion:
    RDP4 = 0x80001
    RDP5 = 0x80004
    RDP10 = 0x80005
    RDP10_1 = 0x80006
    RDP10_2 = 0x80007
    RDP10_3 = 0x80008
    RDP10_4 = 0x80009
    RDP10_5 = 0x8000A
    RDP10_6 = 0x8000B


class ColorDepth:
    RNS_UD_COLOR_4BPP = 0xCA00
    RNS_UD_COLOR_8BPP = 0xCA01
    RNS_UD_COLOR_16BPP_555 = 0xCA02
    RNS_UD_COLOR_16BPP_565 = 0xCA03
    RNS_UD_COLOR_24BPP = 0xCA04


class HighColorDepth:
    HIGH_COLOR_4BPP = 4
    HIGH_COLOR_8BPP = 8
    HIGH_COLOR_15BPP = 15
    HIGH_COLOR_16BPP = 16
    HIGH_COLOR_24BPP = 24


class KeyboardType:
    IBM_PC_XT = 1
    OLIVETTI = 2
    IBM_PC_AT = 3
    IBM_ENHANCED = 4
    NOKIA_1050 = 5
    NOKIA_9140 = 6
    JAPANESE = 7


class SupportedColorDepth:
    RNS_UD_24BPP_SUPPORT = 0x0001
    RNS_UD_16BPP_SUPPORT = 0x0002
    RNS_UD_15BPP_SUPPORT = 0x0004
    RNS_UD_32BPP_SUPPORT = 0x0008


class ClientCapabilityFlag:
    RNS_UD_CS_SUPPORT_ERRINFO_PDU = 0x0001
    RNS_UD_CS_WANT_32BPP_SESSION = 0x0002
    RNS_UD_CS_SUPPORT_STATUSINFO_PDU = 0x0004
    RNS_UD_CS_STRONG_ASYMMETRIC_KEYS = 0x0008
    RNS_UD_CS_UNUSED = 0x0010
    RNS_UD_CS_VALID_CONNECTION_TYPE = 0x0020
    RNS_UD_CS_SUPPORT_MONITOR_LAYOUT_PDU = 0x0040
    RNS_UD_CS_SUPPORT_NETCHAR_AUTODETECT = 0x0080
    RNS_UD_CS_SUPPORT_DYNVC_GFX_PROTOCOL = 0x0100
    RNS_UD_CS_SUPPORT_DYNAMIC_TIME_ZONE = 0x0200
    RNS_UD_CS_SUPPORT_HEARTBEAT_PDU = 0x0400


class ServerCapabilityFlag:
    RNS_UD_SC_EDGE_ACTIONS_SUPPORTED_V1 = 1
    RNS_UD_SC_DYNAMIC_DST_SUPPORTED = 2
    RNS_UD_SC_EDGE_ACTIONS_SUPPORTED_V2 = 4


class ConnectionType:
    CONNECTION_TYPE_MODEM = 0x01
    CONNECTION_TYPE_BROADBAND_LOW = 0x02
    CONNECTION_TYPE_SATELLITE = 0x03
    CONNECTION_TYPE_BROADBAND_HIGH = 0x04
    CONNECTION_TYPE_WAN = 0x05
    CONNECTION_TYPE_LAN = 0x06
    CONNECTION_TYPE_AUTODETECT = 0x07


class DesktopOrientation:
    ORIENTATION_LANDSCAPE = 0
    ORIENTATION_PORTRAIT = 90
    ORIENTATION_LANDSCAPE_FLIPPED = 180
    ORIENTATION_PORTRAIT_FLIPPED = 270


class EncryptionMethod:
    ENCRYPTION_NONE = 0x00
    ENCRYPTION_40BIT = 0x01
    ENCRYPTION_128BIT = 0x02
    ENCRYPTION_56BIT = 0x08
    ENCRYPTION_FIPS = 0x10


class EncryptionLevel:
    ENCRYPTION_LEVEL_NONE = 0
    ENCRYPTION_LEVEL_LOW = 1
    ENCRYPTION_LEVEL_CLIENT_COMPATIBLE = 2
    ENCRYPTION_LEVEL_HIGH = 3
    ENCRYPTION_LEVEL_FIPS = 4


class ClusterFlags:
    REDIRECTION_SUPPORTED = 0x01
    REDIRECTED_SESSIONID_FIELD_VALID = 0x02
    SERVER_SESSION_REDIRECTION_VERSION_MASK = 0x3C
    REDIRECTED_SMARTCARD = 0x40


class RedirectionVersion:
    REDIRECTION_VERSION1 = 0
    REDIRECTION_VERSION2 = 1
    REDIRECTION_VERSION3 = 2
    REDIRECTION_VERSION4 = 3
    REDIRECTION_VERSION5 = 4
    REDIRECTION_VERSION6 = 5


class ServerCertificateType:
    PROPRIETARY = 1
    X509 = 2


class NegotiationProtocols:
    SSL = 0b00000001
    CRED_SSP = 0b00000010
    EARLY_USER_AUTHORIZATION_RESULT = 0b00001000