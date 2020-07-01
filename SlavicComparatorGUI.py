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
    
    # переменные для текста в label'ах
    L1text = StringVar()
    L1text.set(txt)
    L2text = StringVar()
    L3text = StringVar()
    L4text = StringVar()
    L5text = StringVar()
    L6text = StringVar()
    L7text = StringVar()
    L8text = StringVar()
    L9text = StringVar()
    L10text = StringVar()
    L11text = StringVar()
    L12text = StringVar()
    L13text = StringVar()
    L14text = StringVar()
    L15text = StringVar()
    L16text = StringVar()
    L17text = StringVar()
    L18text = StringVar()
    L19text = StringVar()
    L20text = StringVar()
    L21text = StringVar()
    
    # создание самих label'ов
    L1 = Label(window, textvariable = L1text)
    L2 = Label(window, textvariable = L2text)
    L3 = Label(window, textvariable = L3text)
    L4 = Label(window, textvariable = L4text)
    L5 = Label(window, textvariable = L5text)
    L6 = Label(window, textvariable = L6text)
    L7 = Label(window, textvariable = L7text)
    L8 = Label(window, textvariable = L8text)
    L9 = Label(window, textvariable = L9text)
    L10 = Label(window, textvariable = L10text)
    L11 = Label(window, textvariable = L11text)
    L12 = Label(window, textvariable = L12text)
    L13 = Label(window, textvariable = L13text)
    L14 = Label(window, textvariable = L14text)
    L15 = Label(window, textvariable =L15text)
    L16 = Label(window, textvariable = L16text)
    L17 = Label(window, textvariable = L17text)
    L18 = Label(window, textvariable = L18text)
    L19 = Label(window, textvariable = L19text)
    L20 = Label(window, textvariable = L20text)
    L21 = Label(window, textvariable = L21text)
    
    # помещение label'ов в список
    labelsList = [L1, L2, L3, L4, L5, L6, L7, L8,
                  L9, L10, L11, L12, L13, L14, L15,
                  L16, L17, L18, L19, L20, L21]
    

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
