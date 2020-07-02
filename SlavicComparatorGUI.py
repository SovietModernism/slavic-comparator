import SlavicComparatorFunctions as scf   # локальный модуль с функциями
from tkinter import *

# переменная для проверки, была ли уже неудачная попытка ввести слово
anErrorOnceOccured = None

# переменная для проверки, переводилось ли уже что-нибудь
translatedAgain = False

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
    
    global textVariablesList
    
    # создание переменных для хранения текста
    L1t = StringVar()
    L1t.set("Белорусский: ")
    
    L2t = StringVar()
    L2t.set("Украинский: ")
    
    L3t = StringVar()
    L3t.set("Русинский: ")
    
    L4t = StringVar()
    L4t.set("Древнерусский: ")
    
    L6t = StringVar()
    L6t.set("Польский: ")
    
    L7t = StringVar()
    L7t.set("Кашубский: ")
    
    L8t = StringVar()
    L8t.set("Силезский: ")
    
    L9t = StringVar()
    L9t.set("Верхнелужицкий: ")
    
    L10t = StringVar()
    L10t.set("Нижнелужицкий: ")
    
    L11t = StringVar()
    L11t.set("Полабский: ")
    
    L12t = StringVar()
    L12t.set("Чешский: ")
    
    L13t = StringVar()
    L13t.set("Словацкий: ")
    
    L15t = StringVar()
    L15t.set("Словенский: ")
    
    L16t = StringVar()
    L16t.set("Хорватский: ")
    
    L17t = StringVar()
    L17t.set("Сербский: ")
    
    L18t = StringVar()
    L18t.set("Сербохорватский: ")
    
    L19t = StringVar()
    L19t.set("Боснийский: ")
    
    L20t = StringVar()
    L20t.set("Македонский: ")
    
    L21t = StringVar()
    L21t.set("Болгарский: ")
    
    L22t = StringVar()
    L22t.set("Церковнославянский: ")
    
    
    # создание самих label'ов с текстом
    L0 = Label(window, text = "\nВОСТОЧНОСЛАВЯНСКИЕ ЯЗЫКИ\n")
    L1 = Label(window, textvariable = L1t)
    L2 = Label(window, textvariable = L2t)
    L3 = Label(window, textvariable = L3t)
    L4 = Label(window, textvariable = L4t)
    
    L5 = Label(window, text = "\nЗАПАДНОСЛАВЯНСКИЕ ЯЗЫКИ\n")
    L6 = Label(window, textvariable = L6t)
    L7 = Label(window, textvariable = L7t)
    L8 = Label(window, textvariable = L8t)
    L9 = Label(window, textvariable = L9t)
    L10 = Label(window, textvariable = L10t)
    L11 = Label(window, textvariable = L11t)
    L12 = Label(window, textvariable = L12t)
    L13 = Label(window, textvariable = L13t)
    
    L14 = Label(window, text = "\nЮЖНОСЛАВЯНСКИЕ ЯЗЫКИ\n")
    L15 = Label(window, textvariable = L15t)
    L16 = Label(window, textvariable = L16t)
    L17 = Label(window, textvariable = L17t)
    L18 = Label(window, textvariable = L18t)
    L19 = Label(window, textvariable = L19t)
    L20 = Label(window, textvariable = L20t)
    L21 = Label(window, textvariable = L21t)
    L22 = Label(window, textvariable = L22t)
    
    # помещение label'ов и их текстовых переменных в списки
    # первый список служит для размещения label'ов, второй - для изменения их текстовых значений
    labelsGridList = [L0, L1, L2, L3, L4, L5, L6, L7, L8,
                      L9, L10, L11, L12, L13, L14, L15,
                      L16, L17, L18, L19, L20, L21, L22]
    
    textVariablesList = [L1t, L2t, L3t, L4t, L6t, L7t, L8t,
                         L9t, L10t, L11t, L12t, L13t, L15t,
                         L16t, L17t, L18t, L19t, L20t, L21t, L22t]
    
    # размещение label'ов в окне
    a = 3
    b = 3
    c = 3
    
    for i in range(0, 23):
        if i > 4:
            if i > 13:
                labelsGridList[i].grid(column = 2, row = c)
                labelsGridList[i].config(font = ("Times New Roman", 10))
                c += 1
            else:
                labelsGridList[i].grid(column = 1, row = b)
                labelsGridList[i].config(font = ("Times New Roman", 10))
                b += 1
        else:
            labelsGridList[i].grid(column = 0, row = a)
            labelsGridList[i].config(font = ("Times New Roman", 10))
            a += 1


# функия, приводящая текст в label'ах к исходному
def labelsToDefault():

    textVariablesList[0].set("Белорусский: ")
    textVariablesList[1].set("Украинский: ")
    textVariablesList[2].set("Русинский: ")
    textVariablesList[3].set("Древнерусский: ")
    textVariablesList[4].set("Польский: ")
    textVariablesList[5].set("Кашубский: ")
    textVariablesList[6].set("Силезский: ")
    textVariablesList[7].set("Верхнелужицкий: ")
    textVariablesList[8].set("Нижнелужицкий: ")
    textVariablesList[9].set("Полабский: ")
    textVariablesList[10].set("Чешский: ")
    textVariablesList[11].set("Словацкий: ")
    textVariablesList[12].set("Словенский: ")
    textVariablesList[13].set("Хорватский: ")
    textVariablesList[14].set("Сербский: ")
    textVariablesList[15].set("Сербохорватский: ")
    textVariablesList[16].set("Боснийский: ")
    textVariablesList[17].set("Македонский: ")
    textVariablesList[18].set("Болгарский: ")
    textVariablesList[19].set("Церковнославянский: ")


# функция, добавляющая label'ам перевод
def doTranslate():
    
    global translatedAgain
    if translatedAgain:
        labelsToDefault()
    
    translation = ""
    for i in range(0, 20):
        translation = scf.getTranslation(entryWord, scf.language[i])
        textVariablesList[i].set(textVariablesList[i].get() + translation)
    
    translatedAgain = True



# настройки окна
window = Tk()
window.title("Slavic Comparator")
window.geometry('1100x500')
window.resizable(False, False)

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
    entryText.grid(column = 0, row = 0, padx = 10, pady = 10, sticky = "w")
    entryText.config(font = ("Times New Roman", 13, "bold"))

    # строка с вводом
    entryWord = StringVar()    # переменная с текстом, введённым в виджет
    entryWidget = Entry(window, width = 40, textvariable = entryWord)
    entryWidget.grid(column = 1, row = 0, padx = 5, pady = 10)
    entryWidget.config(font = ("Times New Roman", 13))

    # кнопка для начала поиска
    startButton = Button(window, text = "Начать перевод", command = buttonClicked)
    startButton.grid(column = 2, row = 0, padx = 50, pady = 10)
    startButton.config(font = ("Times New Roman", 11))

    # предупреждающий об ошибке текст, если введённое слово неверное
    warningText = Label(window, text = "В слове присутствуют не-кириллические символы либо пробелы!")
    warningText.config(font = ("Times New Roman", 12), fg = "red")
    warningText.grid_forget()

    # отслеживаем лимит
    entryWord.trace("w", lambda *args: character_limit(entryWord))
        
    createLabels()

    window.mainloop
