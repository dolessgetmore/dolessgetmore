from httpimport import *
from httpimport import github_repo

import logging
logging.getLogger('httpimport').setLevel(logging.DEBUG)


with github_repo('dolessgetmore', 'dolessgetmore',['dlgm','game.sound.dog']):
    # import dlgm as gh_dlgm
    import game.sound.dog

print(game.sound.dog)

# print(parse.__author__)