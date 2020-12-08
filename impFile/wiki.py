import wikipedia
import random
import time
from datetime import datetime, timedelta



keyword = [
    "facebook", "spaceX","NASA","perang dunia 2", "perang dunia 1", "indonesia", "braile", "perang dingin","komputer",
    "perancis", "kampus", "manusia", "dinosaurus", "presiden"
]

def Wikipedia(word):
    wikipedia.set_lang('id')
    result = wikipedia.summary(word, sentences = 2)

    return result

