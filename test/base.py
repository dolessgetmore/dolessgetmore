from httpimport import *
from httpimport import github_repo

import logging
logging.getLogger('httpimport').setLevel(logging.DEBUG)


with github_repo('dolessgetmore', 'dolessgetmore', ['dlgm']):
    # import dlgm as gh_dlgm
    import dlgm.dlgm as dlgm

print(dlgm)
# print(parse.__author__)