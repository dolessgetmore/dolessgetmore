from httpimport import *
from httpimport import github_repo

import logging
logging.getLogger('httpimport').setLevel(logging.DEBUG)


from httpimport import github_repo
with github_repo('dolessgetmore', 'dolessgetmore',['dlgm_parser', 'dlgm_driver']):
    from dlgm_parser import Parser as ps
    from dlgm_driver import MyDriver

MyDriver.version