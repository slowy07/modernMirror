# config files

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