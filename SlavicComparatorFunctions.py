import urllib.request
import json
import re


# кастомное исключение при подключении к нерабочему сайту
class noSiteConnectionError(Exception):
    pass

# кортеж, содержащий все сокращения для идентификации языков
language = ('be', 'uk', 'rue', 'orv',  'pl',  'csb', 'szl',
            'hsb',  'dsb',  'pox',  'cs', 'sk',  'sl',
            'hr',  'sr',  'sh',  'bs',  'mk',  'bg',  'cu', )


# кортеж из языков, использующих кириллицу (не включены сербохорватский и церковнославянский)
cyrLanguages = {'uk', 'be', 'rue', 'orv', 'sr', 'bg', 'mk', }


# функция для получения перевода
def getTranslation(entryWord, language2):

    word = entryWord.get()
    wordURL = urllib.parse.quote(word)

    source = "https://iapi.glosbe.com/iapi3/wordlist?l1=ru&l2=" + language2 + \
             "&q=" + wordURL + "&after=1&includeTranslations=true"

    # в словарь собирается информация из запроса
    with urllib.request.urlopen(source) as url:
        data = json.loads(url.read().decode())

    # словарь превращается в строку для возможности её обработки,
    # отсеиваются все лишние элементы, и ключевые слова заносятся в parser
    data = str(data)
    parser = re.sub(r'\,|\{|\}|\[|\]|\:|\: True', '', data)
    parser = re.sub(r'\' \'', '\'', parser)
    parser = re.sub(r' True', '', parser)    # для предотвращения ошибок, когда с первого раза не был убран
    parser = re.sub(r'^\'|\'$', '', parser)
    parser = parser.split("\'")


    # удаление ненужных технических слов
    parser.remove('after')
    parser.remove('phrase')
    parser.remove('translations')
    parser.remove('success')

    # проверка, действительно ли было переведено нужное слово, либо же что-то похожее
    if (parser[0] != word):
        return "нет информации"
    
    else:
        
        # если суммарное число переводов больше 3, при этом
        # второй/третий перевод не совпадает с основным, то его
        # можно включить в выводимый результат
        if (len(parser) >= 3):
            
            if parser[1] != parser[2].lower():
                # если язык перевода использует кириллицу, а перевод не полностью состоит из кириллических букв
                if language2 in cyrLanguages and not isWordCyrillic(parser[2]):
                    return parser[1]
                else:
                    return parser[1] + ' / ' + parser[2]
            
            elif (len(parser) >= 4) and (parser[1] != parser[3].lower()):
                # если язык перевода использует кириллицу, а перевод не полностью состоит из кириллических букв
                if language2 in cyrLanguages and not isWordCyrillic(parser[3]):
                    return parser[1]
                else:
                    return parser[1] + ' / ' + parser[3]
            
            else:
                return parser[1]
            
        else:
            return parser[1]


# функция для проверки наличия интернета и активности сайта
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


# функция для нахождения не-кириллических символов или пробелов в слове
def isEntryCyrillic(entryWord):
    for i in str(entryWord.get()):
        if not bool(re.search('[\u0400-\u04FF]', i)):
            raise StopIteration

def isWordCyrillic(word):
    for i in word:
        if not bool(re.search('[\u0400-\u04FF]', i)) and i != " ":
            return True
        else:
            return False
