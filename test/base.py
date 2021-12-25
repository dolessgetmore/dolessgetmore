from httpimport import *
from httpimport import github_repo

import logging
logging.getLogger('httpimport').setLevel(logging.DEBUG)


with github_repo('dolessgetmore', 'dolessgetmore',['dlgm','parse']):
    import dlgm as dl

a = dl.parse("hi")
print(a)