import urllib.request
import json
import re
from tkinter import *


# кастомное исключение при подключении к нерабочему сайту
class noSiteConnectionError(Exception):
    pass

# переменная для проверки, была ли уже неудачная попытка ввести слово
anErrorOnceOccured = None


# лимит на 30 вводимых символов в строке
def character_limit(entryWord):
    if len(entryWord.get()) > 30:
        entryWord.set(entryWord.get()[:30])


# событие при клике на кнопку поиска
def buttonClicked():
    global anErrorOnceOccured
    global warningText
    try:
        
        for i in str(entryWord.get()):
            if not bool(re.search('[\u0400-\u04FF]', i)):
                raise StopIteration
                
    except StopIteration:
            anErrorOnceOccured = True
            warningText.grid(column = 0, row = 1, padx = 5, columnspan = 2, sticky = "w")
            
    else:
        if anErrorOnceOccured:
            warningText.grid_forget()
        mainProgramPart()
        
        
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


# основная часть программы
def mainProgramPart():
    pass





# настройки окна
window = Tk()
window.title("Slavic Comparator")
window.geometry('1000x500')

# проверка на активность сайта, а также на наличие интернета
try:
    if (urllib.request.urlopen("https://ru.glosbe.com").getcode() != 200):
        raise noSiteConnectionError

except noSiteConnectionError:
    noSiteText = Label(window, text = "Сервер Glosbe работает, однако вернул код ошибки!")
    noSiteText.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = "w")
    noSiteText.config(font = ("Times New Roman", 13), fg = "red")

except urllib.error.URLError:
    noConnectText = Label(window, text = "Этой программе требуется наличие интернета, подключения к которому сейчас нет, либо же сайт Glosbe просто стал недоступен.")
    noConnectText.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = "w")
    noConnectText.config(font = ("Times New Roman", 10), fg = "red")
    
else:
    # начальный текст
    entryText = Label(window, text = "Введите слово на русском:")
    entryText.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = "w")
    entryText.config(font = ("Times New Roman", 13))

    # строка с вводом
    entryWord = StringVar()    # переменная с текстом, введённым в виджет
    entryWidget = Entry(window, width = 40, textvariable = entryWord)
    entryWidget.grid(column = 1, row = 0, padx = 5, pady = 5)
    entryWidget.config(font = ("Times New Roman", 13))

    # кнопка для начала поиска
    startButton = Button(window, text = "Начать перевод", command = buttonClicked)
    startButton.grid(column = 2, row = 0, padx = 40, pady = 5)
    startButton.config(font = ("Times New Roman", 11))

    # предупреждающий об ошибке текст, если введённое слово неверное
    warningText = Label(window, text = "В слове присутствуют не-кириллические символы либо пробелы!")
    warningText.config(font = ("Times New Roman", 12), fg = "red")
    warningText.grid_forget()

    # отслеживаем лимит
    entryWord.trace("w", lambda *args: character_limit(entryWord))

    window.mainloop
