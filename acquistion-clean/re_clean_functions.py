import re

from abbreviations import CARD, ORD, WAY_ABB

def standardize_cardinal(name: str) -> str:
    """
    Function to convert cardinal abbreviations to full names (ex. 'e' -> 'east').
    """
    for card in list(CARD.keys()):
        name = re.sub(f'^{card}\.(?= )|^{card}(?= )|(?<= ){card}\.$|(?<= ){card}$', f'{CARD[card]}', name)
        name = re.sub(f'(?<= ){card}\.(?= )|(?<= ){card}(?= )', f'{CARD[card]}', name)
        name = re.sub(f'(?<= ){card}\.(?![a-z])|(?<= ){card}(?![a-z])', f'{CARD[card]} ', name)
        
    return name

def make_mod_name(name: str) -> str:
    """
    Function to remove ordinal signifiers (ex. '100th' -> '100').
    """
    ordinal = ['st', 'nd', 'rd', 'th']
    for o in ordinal:
        name = re.sub(f'(?<=\d){o}', '', name)
    
    return name

def standardize_way_type(name: str) -> str:
    """
    Function to convert name abbreviations to full names (ex. 'ave' -> 'avenue').
    """
    for way_type in list(WAY_ABB.keys()):
        regex = f'(?<= ){way_type}\.$|(?<= ){way_type}$|(?<= ){way_type}\.(?= )|(?<= ){way_type}(?= )'
        name = re.sub(regex, f'{WAY_ABB[way_type]}', name)

    return name

def ord_to_num(name: str) -> str:
    """
    Function to convert ordinal names to numerical names (ex. 'sixth' -> '6').
    """
    for o in list(ORD.keys()):
        regex = f'^{o}(?= )|(?<= ){o}(?= )|(?<= ){o}$'
        name = re.sub(regex, f'{ORD[o]}', name)

    return name

def clean_saint(name: str) -> str:
    """
    Function to standardize saint (ex. 'st.' -> 'saint').
    """
    name = re.sub(r'^st\.(?= )|^st(?= )', 'saint', name)

    return name