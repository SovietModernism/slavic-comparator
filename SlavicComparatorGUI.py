import SlavicComparatorFunctions as scf   # локальный модуль с функциями
from tkinter import *

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
        
        scf.isCyrillic(entryWord)
                
    except StopIteration:
            anErrorOnceOccured = True
            warningText.grid(column = 0, row = 1, padx = 5, columnspan = 2, sticky = "w")
            
    else:
        if anErrorOnceOccured:
            warningText.grid_forget()
        doTranslate()


# создаёт пустые label'ы-заготовки для языков и вносит их в список
def createLabels():
    
    global labelsList
    
    # создание самих label'ов с текстом
    L0 = Label(window, text = "ВОСТОЧНОСЛАВЯНСКИЕ ЯЗЫКИ")
    L1 = Label(window, text = "Белорусский:")
    L2 = Label(window, text = "Украинский:")
    L3 = Label(window, text = "Русинский:")
    L4 = Label(window, text = "Древнерусский:")
    
    L5 = Label(window, text = "\nЗАПАДНОСЛАВЯНСКИЕ ЯЗЫКИ")
    L6 = Label(window, text = "Польский:")
    L7 = Label(window, text = "Кашубский:")
    L8 = Label(window, text = "Силезский:")
    L9 = Label(window, text = "Верхнелужицкий:")
    L10 = Label(window, text = "Нижнелужицкий:")
    L11 = Label(window, text = "Полабский:")
    L12 = Label(window, text = "Чешский:")
    L13 = Label(window, text = "Словацкий:")
    
    L14 = Label(window, text = "\nЮЖНОСЛАВЯНСКИЕ ЯЗЫКИ")
    L15 = Label(window, text = "Словенский:")
    L16 = Label(window, text = "Хорватский:")
    L17 = Label(window, text = "Сербский:")
    L18 = Label(window, text = "Сербохорватский:")
    L19 = Label(window, text = "Боснийский:")
    L20 = Label(window, text = "Македонский:")
    L21 = Label(window, text = "Болгарский:")
    L22 = Label(window, text = "Церковнославянский:")
    
    # помещение label'ов в список
    labelsList = [L0, L1, L2, L3, L4, L5, L6, L7, L8,
                  L9, L10, L11, L12, L13, L14, L15,
                  L16, L17, L18, L19, L20, L21, L22]
    
    # размещение label'ов в цикле
    for i in range(0, 23):
        labelsList[i].grid(column = 0, row = i+3)
    

# основная часть программы
def doTranslate():
    pass





# настройки окна
window = Tk()
window.title("Slavic Comparator")
window.geometry('1000x500')

# проверка на активность сайта, а также на наличие интернета
if scf.isConnected() == "noSiteConnectionError":
    noSiteText = Label(window, text = "Сервер Glosbe работает, однако вернул код ошибки!")
    noSiteText.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = "w")
    noSiteText.config(font = ("Times New Roman", 13), fg = "red")
    
elif scf.isConnected() == "urllib.error.URLError":
    noConnectText = Label(window, text = "Этой программе требуется наличие интернета, подключения к которому сейчас нет, либо же сайт Glosbe просто стал недоступен.")
    noConnectText.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = "w")
    noConnectText.config(font = ("Times New Roman", 10), fg = "red")
    
elif scf.isConnected() == "yes":
 
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
    
    createLabels()

    window.mainloop
