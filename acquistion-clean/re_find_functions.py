import re

from zipcodes import ZIPCODES

def has_num(name: str) -> str | None:
    """
    Function to determine if street name has numerical value.
    """
    match = re.search(r'\d+', name)
    if match is not None:
        return match.group()
    
    return None

def has_way_type(name: str) -> str | None:
    """
    Function to determine if street name has a 'way' type (ex. 'avenue').
    """
    way_types = [
        'avenue', 'road', 'street',
        'boulevard', 'place', 'drive',
        'lane', 'expressway', 'square',
        'court', 'parkway', 'terrace'
    ]
    for wt in way_types:
        if re.search(f'.* {wt}', name):
            return wt
    for wt in way_types:
        if re.search(f'.* {wt} .*', name):
            return wt
    
    return None

def get_way_name(name: str) -> str | None:
    """
    Function to determine if street name has a cardinal value (ex. 'west').
    """
    cards = ['north', 'east', 'south', 'west', 'northeast', 'southeast', 'northwest', 'southwest']
    way_types = [
        'avenue', 'road', 'street',
        'boulevard', 'place', 'drive',
        'lane', 'expressway', 'square',
        'court', 'parkway'
    ]
    remove_words = cards + way_types
    name = re.sub(r'\d+', '', name)
    for word in remove_words:
        name = re.sub(f'^{word} ', ' ', name)
        name = re.sub(f' {word}$', ' ', name)
        name = re.sub(f' {word} ', ' ', name)

    name = name.strip()
    if name != '':
        return name
    return None

def has_cardinal(name: str) -> tuple[str]:
    cards = ['north', 'east', 'south', 'west', 'northeast', 'southeast', 'northwest', 'southwest']
    card_loc = [None, None, None]
    for card in cards:
        if re.match(f'^({card} ).*', name):
            card_loc[0] = card
        if re.match(f'^(?!{card}).*( {card} ).*(?!{card}).$', name):
            card_loc[1] = card
        if re.match(f'.*( {card})$', name):
            card_loc[2] = card
    card_loc = tuple(card_loc)
    
    return card_loc

def is_film_boro(film_zcs: list[str], boro: str) -> bool:
    """
    Function to determine in a borough is involved in a film permit.
    """
    boro_zcs = ZIPCODES[boro]
    for zc in film_zcs:
        if zc in boro_zcs:
            return True
    
    return False