# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
from typing import Literal


def alphabetical_order(list_):
    return sorted(list_)

def won_golden_globe(items):
    golden_globe_win = ['jaws', 'star wars: episode iv – a new hope', 'e.t. the extra-terrestrial', 'memoirs of a geisha']
    if items.lower() in golden_globe_win:
        return True
    else: 
        return False


def remove_toto_albums(list_strings):
    toto_albums = ['Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between', '35th Anniversary - Live in Poland', 'Toto XIV', 'Old Is New', '40 Tours Around the Sun', 'With a Little Help from My Friends']

    newList_ = [x for x in list_strings if x not in toto_albums]
    # newList = list(set(list_strings) - set(toto_albums))
    return newList_

        


 
print(remove_toto_albums(['The Seventh One', 'Enne', 'Toto XX']))