import wikipedia
import random
import time
from datetime import datetime, timedelta



keyword = [
    "facebook", "spaceX","NASA","perang dunia 2", "perang dunia 1", "indonesia", "braile", "perang dingin","komputer",
    "perancis", "kampus", "manusia", "dinosaurus", "presiden","google","ular","buaya","komodo","VOC","pancasila",
    "FBI","CIA", "kamus", "bilangan biner", "alan turing", "laptop", "tom and jerry", "kamera",
    "apple","google","programmer","polisi","tentara","BIN","BMW","Ferrari","GIGN","Kopassus","GIGN",
    "game","microsoft","windows","linux","android","symbian","mamalia","jam matahari","pasta gigi",
    "kriptografi","cuaca","gempa","tornado","longsor","bank","cinta","soekarno","bus","ponsel pintar",
    "SAS","Hacker", "Nikola Tesla", "Albert Einstein"
]

def Wikipedia(word):
    wikipedia.set_lang('id')
    result = wikipedia.summary(word, sentences = 2)

    return result
