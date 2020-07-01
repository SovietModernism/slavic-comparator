import urllib.request
import json
import re


# кастомное исключение при подключении к нерабочему сайту
class noSiteConnectionError(Exception):
    pass
        
        
# функция для получения перевода
def getTranslation(wordURL, language2):

    source = "https://iapi.glosbe.com/iapi3/wordlist?l1=ru&l2=" + language2 + \
             "&q=" + wordURL + "&after=1&includeTranslations=true"

    # в словарь собирается информация из запроса
    with urllib.request.urlopen(source) as url:
        data = json.loads(url.read().decode())

    # словарь превращается в строку, отсеиваются все слова
    data = str(data)
    parser = re.findall(r'\w+', data)

    # удаление ненужных технических слов
    parser.remove('after')
    parser.remove('phrase')
    parser.remove('translations')
    parser.remove('success')
    parser.remove('True')

    # проверка, действительно ли было переведено нужное слово, либо же что-то похожее
    if (parser[0] != word):
        return "нет информации"
    else:
        # дополнительные переводы включаются в результат, если те не совпадают с основным переводом
        if (len(parser) >= 3):
            if parser[1] != parser[2].lower():
                return parser[1] + ' / ' + parser[2]
            elif (len(parser) >= 4) and (parser[1] != parser[3].lower()):
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
def isCyrillic(entryWord):
    for i in str(entryWord.get()):
            if not bool(re.search('[\u0400-\u04FF]', i)):
                raise StopIteration