from enum import Enum


class Language(Enum):
    ENGLISH = 'English'
    CHINESE = 'Chinese'
    MALAY = 'Malay'
    TAMIL = 'Tamil'


class MediaCode(Enum):
    """
    Title Level Media Code and Media Description Mapping

    http://www.nlb.gov.sg/labs/technical-documentation/#TitleLevelMediaCodeandMediaDescriptionMapping
    """
    BOOKS = 'BK'
    COMPUTER_FILE = 'CF'
    MAPS = 'MP'
    MUSIC = 'MU'
    MIXED_MATERIALS = 'MX'
    SERIALS = 'SE'
    VISUAL_MATERIALS = 'VM'


class Branch(Enum):
    """
    Branch Code and Branch Name Mapping

    http://www.nlb.gov.sg/labs/technical-documentation/#BranchCodeandBranchNameMapping
    """
    TAMPINES_REGIONAL_LIBRARY = 'TRL'
    WOODLANDS_REGIONAL_LIBRARY = 'WRL'
    CLEMENTI_PUBLIC_LIBRARY = 'CMPL'
    LEE_KONG_CHIAN_REFERENCE_LIBRARY = 'LKCRL'
    ANG_MO_KIO_PUBLIC_LIBRARY = 'AMKPL'
    BUKIT_BATOK_PUBLIC_LIBRARY = 'BBPL'
    BUKIT_PANJANG_PUBLIC_LIBRARY = 'BPPL'
    BUKIT_MERAH_PUBLIC_LIBRARY = 'BMPL'
    CENTRAL_PUBLIC_LIBRARY = 'CLL'
    CHENG_SAN_PUBLIC_LIBRARY = 'CSPL'
    CHOA_CHU_KANG_PUBLIC_LIBRARY = 'CCKPL'
    GEYLANG_EAST_PUBLIC_LIBRARY = 'GEPL'
    JURONG_REGIONAL_LIBRARY = 'JRL'
    JURONG_WEST_PUBLIC_LIBRARY = 'JWPL'
    QUEENSTOWN_PUBLIC_LIBRARY = 'QUPL'
    TOA_PAYOH_PUBLIC_LIBRARY = 'TPPL'
    YISHUN_PUBLIC_LIBRARY = 'YIPL'
    LIBRARY_AT_ORCHARD = 'OCPL'
    LIBRARY_AT_CHINATOWN = 'CNPL'
    SEMBAWANG_PUBLIC_LIBRARY = 'SBPL'
    LIBRARY_SUPPLY_CENTRE = 'LSC'
    SERANGOON_PUBLIC_LIBRARY = 'SRPL'
    NL_HERITAGE = 'LOLC'
    MARINE_PARADE_PUBLIC_LIBRARY = 'MPPL'
    BEDOK_PUBLIC_LIBRARY = 'BEPL'
    SENGKANG_PUBLIC_LIBRARY = 'SKPL'
    LIBRARY_AT_ESPLANADE = 'EPPL'
    MOBILE_BUS = 'MOLLEY'
    PASIR_RIS_PUBLIC_LIBRARY = 'PRPL'
    BISHAN_PUBLIC_LIBRARY = 'BIPL'
    LIBRARY_SUPPLY_CENTRE_FOR_AV = 'LSCAV'
    LEE_KONG_CHIAN_REFERENCE_LIBRARY_LEVEL_7 = '07LKCRL'
    LEE_KONG_CHIAN_REFERENCE_LIBRARY_LEVEL_8 = '08LKCRL'
    LEE_KONG_CHIAN_REFERENCE_LIBRARY_LEVEL_9 = '09LKCRL'
    LEE_KONG_CHIAN_REFERENCE_LIBRARY_LEVEL_11 = '11LKCRL'


class Sort(Enum):
    PUBDATE = 'PUBDATE'
    TITLE = 'TITLE'
