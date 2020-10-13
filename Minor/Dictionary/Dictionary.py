import json
from difflib import get_close_matches

data=json.load(open("data.json")) #converting json objects to python dictionary

def search(word):
    word=word.lower()
    if word in data:
        return(data[word])
        
    elif word.title() in data:
        return(data[word.title()])

    elif word.upper() in data:
        return(data[word.upper()])

    elif len(get_close_matches(word , data.keys())) > 0 :
        print("Did you meant %s?\n" %get_close_matches(word, data.keys())[0])
        decide = input()
        if decide.lower() == "y" or decide.lower()=='yes':
            return data[get_close_matches(word , data.keys())[0]]
        else:
            return("\nThen you have typed incorrectly! Check your spelling!")

    else:
        #by default none is returned if no search result is found
        return('The word you wanted to search was not found!')


word=input('Enter the word to be searched-> ')
print()
output=search(word)
if(type(output)==list):
    for item in output:
        print(item)
else:
    print(output)