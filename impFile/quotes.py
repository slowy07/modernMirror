import wikiquote
import random

personName = ["Linus Torvalds", "Mark Zuckerberg"]

def quoteToday(person):
    quote = random.choice(wikiquote.quotes(person))

    return quote