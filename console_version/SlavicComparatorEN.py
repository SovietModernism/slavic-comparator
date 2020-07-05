import urllib.request
import json
import re
import os


# custom exception occuring when Glosbe site returned any code but 200
class noSiteConnectionError(Exception):
    pass

# tuple of languages using Cyrillic script (Serbocroatian and Church Slavonic are not included)
cyrLanguages = {'ru', 'be', 'uk', 'rue', 'orv', 'sr', 'bg', 'mk', }


def getTranslation(word, language2):

    source = "https://iapi.glosbe.com/iapi3/wordlist?l1=en&l2=" + language2 + \
             "&q=" + word + "&after=1&includeTranslations=true"

    # gathering all the information to the list
    with urllib.request.urlopen(source) as url:
        data = json.loads(url.read().decode())

    # list is turned into a string to use regexp on it.
    # excess elements are removed, parser takes the key words
    data = str(data)
    parser = re.sub(r'\,|\{|\}|\[|\]|\:|\: True', '', data)
    parser = re.sub(r'\' \'', '\'', parser)
    parser = re.sub(r' True', '', parser)    # to prevent possible bug
    parser = re.sub(r'^\'|\'$', '', parser)
    parser = parser.split("\'")

    # deleting unnecessary technical words
    parser.remove('after')
    parser.remove('phrase')
    parser.remove('translations')
    parser.remove('success')

    # check if it's the right word which was translated
    if (parser[0] != word):
        return "no info"

    else:

        # if the total number of words is more than 3, we can try
        # to include 2 translations to the final result instead
        # of just one, but only if they're different
        if (len(parser) >= 3):

            if parser[1] != parser[2].lower():
                # if the 2nd language uses Cyrillic script, but the translated word has some different letters
                if language2 in cyrLanguages and not isFullyCyrillic(parser[2]):
                    return parser[1]
                else:
                    return parser[1] + ' / ' + parser[2]

            elif (len(parser) >= 4) and (parser[1] != parser[3].lower()):
                # if the 2nd language uses Cyrillic script, but the translated word has some different letters
                if language2 in cyrLanguages and not isFullyCyrillic(parser[3]):
                    return parser[1]
                else:
                    return parser[1] + ' / ' + parser[3]

            else:
                return parser[1]

        else:
            return parser[1]


# check if word is written in Cyrillic only (whitespaces allowed)
def isFullyCyrillic(text):
    try:
            for i in text:
                if not bool(re.search('[\u0400-\u04FF]', i)) and i != " ":
                    raise StopIteration

    except StopIteration:
        # the loop was interrupted -> has non-Cyrillic letters
        return False

    else:
        # the loop wasn't interrupted -> is fully Cyrillic
        return True


# check if word is written in Latin only (whitespaces NOT allowed, it's for input)
def isFullyLatin(text):
    try:
            for i in text:
                if not bool(re.search('[\u0041-\u005A]|[\u0061-\u007A]', i)):
                    raise StopIteration

    except StopIteration:
        # the loop was interrupted -> has non-Latin letters
        return False

    else:
        # the loop wasn't interrupted -> is fully Latin
        return True


try:
    if (urllib.request.urlopen("https://en.glosbe.com").getcode() != 200):   # check the site's activity
        raise noSiteConnectionError

except noSiteConnectionError:
    print("Glosbe site is up right now, but it returned an error code!")
    os.system("pause")

except urllib.error.URLError:
    print("This program requires having an Internet connection (which isn't now), or Glosbe site just suddenly got down")
    os.system("pause")

else:
    while (True):

        while(True):    # check if word is normal
            print("Input a word in English:")
            word = input()

            if len(word) <= 30:
                if isFullyLatin(word):

                    #word = urllib.parse.quote(word)
                    break

                else:
                    print("Your word has whitespaces or non-Latin letters, try again.")
            else:
                print("The word is too long.")

        try:
            print("\nEAST SLAVIC LANGUAGES\n")
            
            print("Russian: ", getTranslation(word, 'ru'))
            print("Belorussian: ", getTranslation(word, 'be'))
            print("Ukrainian: ", getTranslation(word, 'uk'))
            print("Rusyn: ", getTranslation(word, 'rue'))
            print("Old Russian: ", getTranslation(word, 'orv'))

            print("\nWEST SLAVIC LANGUAGES\n")

            print("Polish: ", getTranslation(word, 'pl'))
            print("Kashubian: ", getTranslation(word, 'csb'))
            print("Silesian: ", getTranslation(word, 'szl'))
            print("Upper Sorbian: ", getTranslation(word, 'hsb'))
            print("Lower Sorbian: ", getTranslation(word, 'dsb'))
            print("Polabian: ", getTranslation(word, 'pox'))
            print("Czech: ", getTranslation(word, 'cs'))
            print("Slovak: ", getTranslation(word, 'sk'))

            print("\nSOUTH SLAVIC LANGUAGES\n")

            print("Slovenian: ", getTranslation(word, 'sl'))
            print("Croatian: ", getTranslation(word, 'hr'))
            print("Serbian: ", getTranslation(word, 'sr'))
            print("Serbocroatian: ", getTranslation(word, 'sh'))
            print("Bosnian: ", getTranslation(word, 'bs'))
            print("Macedonian: ", getTranslation(word, 'mk'))
            print("Bulgarian: ", getTranslation(word, 'bg'))
            print("Church Slavonic: ", getTranslation(word, 'cu'))

            print("\nChoose a new word? (yes / anything else)")
            word = input()
            if (word != 'yes'):
                break
            else:
                os.system('cls')

        # may happen during getTranslation function, on the "removing unnecessary words" stage,
        # if there the program tries to remove a word parser doesn't have
        except ValueError:
            print("An error occured while processing abnormal data.")
            os.system("pause")
            break

        # may happen when urllib module is trying to work with site, but there is no Internet
        except urllib.error.URLError:
            print("Internet connection was lost during program execution.")
            os.system("pause")
            break

        # catch all the other exceptions
        except:
            print("Unexpected error occured.")
            os.system("pause")
            break
