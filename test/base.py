from httpimport import *
from httpimport import github_repo

import logging
logging.getLogger('httpimport').setLevel(logging.DEBUG)


with github_repo('dolessgetmore', 'dolessgetmore',['dlgm','parse']):
    # import dlgm as gh_dlgm
    import dlgm

print(dlgm.parse)

# print(parse.__author__)