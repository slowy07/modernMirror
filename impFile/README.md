# config files
[wikipedia](https://github.com/slowy07/modernMirror/blob/main/impFile/README.md#wikipedia)
[quotes](https://github.com/slowy07/modernMirror/tree/main/impFile#quotes)

# wikipedia
[wiki](https://github.com/slowy07/modernMirror/blob/main/impFile/wiki.py) generate wikipedia search result
example print all summary about google corporation
```python
import wikipedia 
print(wikipedia.summary("google corporation"))
```
using ```page()``` function
```python
import wikipedia
information = wikipedia.page("indonesia")
print(information.title) #displaying title
print(information.url) #displaying url
print(information.content) #displaying content about indonesia
```
change language
```python
import wikipedia
wikipedia.set_lang("id") #country code for displaying language country
print(wikipedia.summary("google corporation"))
```
change paragraph of summary content
```python 
import wikipedia
wikipedia.set_lang("id")
print(wikipedia.summary("google corporation", sentences = 2))
```

## quotes
installation
```bash
sudo pip install --upgrade wikiquote
```
usage
```python
import wikiquote
print(wikiquote.quotes('Linus Torvalds'))
```
using ``random()`` for random quotes from list of ``personName``
```python
import wikiquote
import random
personName = ['Mark Zuckerberg','Aristotle','Plato','Socrates']
print(wikiquote.quotes(random.choice(personName)))
```
for more information about quotes here : [wikiquote](https://github.com/federicotdn/wikiquote)
