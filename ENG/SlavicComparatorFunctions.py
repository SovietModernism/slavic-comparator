import urllib.request
import json
import re


# custom exception occuring when Glosbe returned any code but 200 (site is down)
class noSiteConnectionError(Exception):
    pass

# tuple containing all abbreviations for languages identification
language = ('be', 'uk', 'rue', 'orv',  'pl',  'csb', 'szl',
            'hsb',  'dsb',  'pox',  'cs', 'sk',  'sl',
            'hr',  'sr',  'sh',  'bs',  'mk',  'bg',  'cu', )


# tuple of languages using Cyrillic script (Serbocroatian and Church Slavonic not included)
cyrLanguages = {'uk', 'be', 'rue', 'orv', 'sr', 'bg', 'mk', }


# function for getting one single translation
def getTranslation(entryWord, language2):

    word = entryWord.get()
    wordURL = urllib.parse.quote(word)

    source = "https://iapi.glosbe.com/iapi3/wordlist?l1=ru&l2=" + language2 + \
             "&q=" + wordURL + "&after=1&includeTranslations=true"

    # gathering all the information to the list
    with urllib.request.urlopen(source) as url:
        data = json.loads(url.read().decode())

    # dictionary turns into string so we can use regex on it.
    # excess elements are removed, parser takes the key words
    data = str(data)
    parser = re.sub(r'\,|\{|\}|\[|\]|\:|\: True', '', data)
    parser = re.sub(r'\' \'', '\'', parser)
    parser = re.sub(r' True', '', parser)    # to prevent possible bug, when wasn't removed in 1st regex
    parser = re.sub(r'^\'|\'$', '', parser)
    parser = parser.split("\'")


    # removing unnecessary technical words
    parser.remove('after')
    parser.remove('phrase')
    parser.remove('translations')
    parser.remove('success')

    # check if we translated the right word, or it was just something similar
    if (parser[0] != word):
        return "нет информации"

    else:

        # if the total number of words is more than 3, we can try
        # to include 2 translations to the final result instead
        # of just one, but only if they're different
        if (len(parser) >= 3):
            
            if parser[1] != parser[2].lower():
                # if the 2nd language uses Cyrillic script, but the translated word has some different letters
                if language2 in cyrLanguages and not isWordCyrillic(parser[2]):
                    return parser[1]
                else:
                    return parser[1] + ' / ' + parser[2]
            
            elif (len(parser) >= 4) and (parser[1] != parser[3].lower()):
                # if the 2nd language uses Cyrillic script, but the translated word has some different letters
                if language2 in cyrLanguages and not isWordCyrillic(parser[3]):
                    return parser[1]
                else:
                    return parser[1] + ' / ' + parser[3]
            
            else:
                return parser[1]
            
        else:
            return parser[1]


# check if there is Internet and Glosbe is online
def isConnected():
    try:
        if (urllib.request.urlopen("https://ru.glosbe.com").getcode() != 200):
            raise noSiteConnectionError

    except noSiteConnectionError:
        return "noSiteConnectionError"

    except urllib.error.URLError:
        return "urllib.error.URLError"
    else:
        return "yes"


# function for finding non-Cyrillic letters in input
def isEntryCyrillic(entryWord):
    for i in str(entryWord.get()):
        if not bool(re.search('[\u0400-\u04FF]', i)):
            raise StopIteration

# same, but for usual words, not the input
def isWordCyrillic(word):
    for i in word:
        if not bool(re.search('[\u0400-\u04FF]', i)) and i != " ":
            return False
        else:
            return True
