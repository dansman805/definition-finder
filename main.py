import requests, bs4, bleach, pyperclip

word = raw_input('What word do you want the definition for?\n')
url = 'http://www.dictionary.com/browse/' + word
res = requests.get(url)

soup = bs4.BeautifulSoup(res.text, 'lxml')

#First definition is found at <div class="def-content">
defContents = soup.select('.def-content')

try:
    __ = defContents[0]
except:
    print '\nThat definition is not available.'
    quit()

definitionHTML = str(defContents[0])

#Getting rid of HTML tags from definition
definition = bleach.clean(definitionHTML, tags=[], strip=True)

#Get rid of trailing/leading whitespace
definition = definition.strip()

#Display definition
print '\n' + definition

#Copy definition to clipboard
pyperclip.copy(definition)