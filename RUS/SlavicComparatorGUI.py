import SlavicComparatorAdditional as sca   # локальный модуль с функциями
import urllib.error
from tkinter import *
from ctypes import windll


class App(Tk):
    
    # переменная для проверки, была ли уже неудачная попытка ввести слово
    anErrorOnceOccured = None

    # переменная для проверки, переводилось ли уже что-нибудь
    translatedAgain = False

    
    # лимит на 30 вводимых символов в строке
    def character_limit(self, entryWord):
        if len(entryWord.get()) > 30:
            entryWord.set(entryWord.get()[:30])
                
                
    # событие при клике на кнопку поиска
    def buttonClicked(self):

        try:
            sca.isEntryCyrillic(self.entryWord)
                
        except StopIteration:
            self.anErrorOnceOccured = True
            self.warningText.config(text = "В слове присутствуют не-кириллические символы либо пробелы!")
            self.warningText.place(x = 50, y = 425)

        else:
            if self.anErrorOnceOccured:
                self.warningText.place_forget()
            self.doTranslate()
                
                
    # создаёт пустые label'ы-заготовки для языков и вносит их в список
    def createLabels(self):

        # создание переменных для хранения текста и их инициализация
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
        L0 = Label(self, text = "ВОСТОЧНОСЛАВЯНСКИЕ ЯЗЫКИ")
        L1 = Label(self, textvariable = L1t)
        L2 = Label(self, textvariable = L2t)
        L3 = Label(self, textvariable = L3t)
        L4 = Label(self, textvariable = L4t)

        L5 = Label(self, text = "ЗАПАДНОСЛАВЯНСКИЕ ЯЗЫКИ")
        L6 = Label(self, textvariable = L6t)
        L7 = Label(self, textvariable = L7t)
        L8 = Label(self, textvariable = L8t)
        L9 = Label(self, textvariable = L9t)
        L10 = Label(self, textvariable = L10t)
        L11 = Label(self, textvariable = L11t)
        L12 = Label(self, textvariable = L12t)
        L13 = Label(self, textvariable = L13t)

        L14 = Label(self, text = "ЮЖНОСЛАВЯНСКИЕ ЯЗЫКИ")
        L15 = Label(self, textvariable = L15t)
        L16 = Label(self, textvariable = L16t)
        L17 = Label(self, textvariable = L17t)
        L18 = Label(self, textvariable = L18t)
        L19 = Label(self, textvariable = L19t)
        L20 = Label(self, textvariable = L20t)
        L21 = Label(self, textvariable = L21t)
        L22 = Label(self, textvariable = L22t)

        # помещение label'ов и их текстовых переменных в списки
        # первый список служит для размещения label'ов, второй - для изменения их текстовых значений
        labelsPlaceList = [L0, L1, L2, L3, L4, L5, L6, L7, L8,
                          L9, L10, L11, L12, L13, L14, L15,
                          L16, L17, L18, L19, L20, L21, L22]

        self.textVariablesList = [L1t, L2t, L3t, L4t, L6t, L7t, L8t,
                             L9t, L10t, L11t, L12t, L13t, L15t,
                             L16t, L17t, L18t, L19t, L20t, L21t, L22t]

        # размещение label'ов в окне, а также задание им шрифта
        a = 150    # восточнославянские
        b = 150    # западнославянские
        c = 150    # южнославянские

        for i in range(0, 23):

            labelsPlaceList[i].config(font = ("Times New Roman", 11))

            if i > 4:
                if i > 13:
                    labelsPlaceList[i].place(x = 975, y = c)
                    c += 25
                else:
                    labelsPlaceList[i].place(x = 525, y = b)
                    b += 25
            else:
                labelsPlaceList[i].place(x = 50, y = a)
                a += 25

        # отдельное переразмещение label'ов с названиями языковых групп
        labelsPlaceList[0].place(x = 50, y = 130)
        labelsPlaceList[5].place(x = 525, y = 130)
        labelsPlaceList[14].place(x = 975, y = 130)


    # функция, приводящая текст в label'ах к исходному
    def labelsToDefault(self):

        self.textVariablesList[0].set("Белорусский: ")
        self.textVariablesList[1].set("Украинский: ")
        self.textVariablesList[2].set("Русинский: ")
        self.textVariablesList[3].set("Древнерусский: ")
        self.textVariablesList[4].set("Польский: ")
        self.textVariablesList[5].set("Кашубский: ")
        self.textVariablesList[6].set("Силезский: ")
        self.textVariablesList[7].set("Верхнелужицкий: ")
        self.textVariablesList[8].set("Нижнелужицкий: ")
        self.textVariablesList[9].set("Полабский: ")
        self.textVariablesList[10].set("Чешский: ")
        self.textVariablesList[11].set("Словацкий: ")
        self.textVariablesList[12].set("Словенский: ")
        self.textVariablesList[13].set("Хорватский: ")
        self.textVariablesList[14].set("Сербский: ")
        self.textVariablesList[15].set("Сербохорватский: ")
        self.textVariablesList[16].set("Боснийский: ")
        self.textVariablesList[17].set("Македонский: ")
        self.textVariablesList[18].set("Болгарский: ")
        self.textVariablesList[19].set("Церковнославянский: ")


    # функция, добавляющая label'ам перевод
    def doTranslate(self):

        # возврат к исходным значениям, чтобы переводы
        # не накладывались друг на друга
        if self.translatedAgain:
            self.labelsToDefault()

        translation = ""
        for i in range(0, 20):
            try:
                translation = sca.getTranslation(self.entryWord, sca.language[i])
                self.textVariablesList[i].set(self.textVariablesList[i].get() + translation)
                
            except urllib.error.URLError:
                self.warningText.config(text = "Отсутствует подключение к интернету, или же сайт Glosbe просто стал недоступен.")
                self.warningText.place(x = 50, y = 425)
                break
            
            except:
                self.warningText.config(text = "Произошла непредвиденная ошибка!")
                self.warningText.place(x = 50, y = 425)
                break

        self.translatedAgain = True

    
    def __init__(self): 
        super().__init__()

        # начальный текст
        entryText = Label(self, text = "Введите слово на русском:")
        entryText.place(x = 555, y = 10)
        entryText.config(font = ("Times New Roman", 14))
 
        # строка с вводом
        self.entryWord = StringVar()
        entryWidget = Entry(self, width = 40, textvariable = self.entryWord)
        entryWidget.place(x = 475, y = 55)
        entryWidget.config(font = ("Times New Roman", 13))

        # кнопка для начала поиска
        startButton = Button(self, text = "Начать перевод", command = self.buttonClicked)
        startButton.place(x = 950, y = 52.5)
        startButton.config(font = ("Times New Roman", 11))

        # предупреждающий об ошибке текст, если введённое слово неверное
        self.warningText = Label(self)
        self.warningText.place(x = 50, y = 425)
        self.warningText.config(font = ("Times New Roman", 12), fg = "red")
        self.warningText.place_forget()
        
        # отслеживаем лимит
        self.entryWord.trace("w", lambda *args: self.character_limit(self.entryWord))

        self.createLabels()


# запуск GUI
if __name__ == "__main__": 
    root = App()

    root.geometry('1500x475')
    root.resizable(False, False)

    # стандартизация размера и DPI окна для всех вариантов выполнения программы
    root.call('tk', 'scaling', 1.7)
    windll.shcore.SetProcessDpiAwareness(1)
    
    root.title("Slavic Comparator")
    
    root.mainloop()