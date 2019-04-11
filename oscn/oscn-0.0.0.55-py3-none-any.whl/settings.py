

OSCN_CASE_URL = "https://www.oscn.net/dockets/GetCaseInformation.aspx"
OSCN_SEARCH_URL = "https://www.oscn.net/dockets/Results.aspx"

OSCN_REQUEST_HEADER = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9'
        }

REMOVE_TITLES = ['HONORABLE']

INVALID_CASE_MESSAGES = [
    "Case Number is Invalid",
    ]
UNUSED_CASE_MESSAGES = [
    "SKIPPED IN ERROR",
    "Something went wrong",
    'THIS CASE NUMBER WAS NOT USED',
    "is formatted incorrectly or is not found within",
    ">No Record.</td>"
    ]

# How many empty cases in a row to decide we're at the end of the case list?
MAX_EMPTY_CASES = 10


ALL_COURTS = [
    'adair',
    'alfalfa',
    'appellate',
    'atoka',
    'beaver',
    'beckham',
    'blaine',
    'bryan',
    'caddo',
    'canadian',
    'carter',
    'cherokee',
    'choctaw',
    'cimarron',
    'cleveland',
    'coal',
    'comanche',
    'cotton',
    'craig',
    'creek',
    'bristow',
    'drumright',
    'custer',
    'delaware',
    'dewey',
    'ellis',
    'garfield',
    'garvin',
    'grady',
    'grant',
    'greer',
    'harmon',
    'harper',
    'haskell',
    'hughes',
    'jackson',
    'jefferson',
    'johnston',
    'kay',
    'poncacity',
    'kingfisher',
    'kiowa',
    'latimer',
    'leflore',
    'lincoln',
    'logan',
    'love',
    'major',
    'marshall',
    'mayes',
    'mcclain',
    'mccurtain',
    'mcintosh',
    'murray',
    'muskogee',
    'noble',
    'nowata',
    'okfuskee',
    'oklahoma',
    'okmulgee',
    'henryetta',
    'osage',
    'ottawa',
    'payne',
    'pawnee',
    'pittsburg',
    'pontotoc',
    'pottawatomie',
    'pushmataha',
    'rogermills',
    'rogers',
    'seminole',
    'sequoyah',
    'stephens',
    'texas',
    'tillman',
    'tulsa',
    'wagoner',
    'washington',
    'washita',
    'woods',
    'woodward']
