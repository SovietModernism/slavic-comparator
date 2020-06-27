import re
from tkinter import *

anErrorOnceOccured = None

def character_limit(entry_word):
    if len(entry_word.get()) > 30:
        entry_word.set(entry_word.get()[:30])

# событие при клике на кнопку поиска
def buttonClicked():
    try:
        for i in str(entry_word.get()):
            if not bool(re.search('[\u0400-\u04FF]', i)):
                raise StopIteration
                
    except StopIteration:
        warningText = Label(window, text = "В слове присутствуют не-кириллические символы либо пробелы!")
        warningText.grid(column = 0, row = 2)
        warningText.config(font = ("Times New Roman", 11), fg = "red")
        anErrorOnceOccured = True
    else:
        mainProgramPart()


# основная часть программы
def mainProgramPart():
    if anErrorOnceOccured:
        warningText.destroy()

# настройки окна
window = Tk()
window.title("Slavic Comparator")
window.geometry('1000x500')

# начальный текст
entryText = Label(window, text = "Введите слово на русском:", font = ("Times New Roman", 13))
entryText.grid(column = 0, row = 0, padx = 5, pady = 5)

# строка с вводом
entry_word = StringVar()    # переменная с текстом, введённым в виджет
entry_widget = Entry(window, width = 40, textvariable = entry_word)
entry_widget.grid(column = 1, row = 0, pady = 5)
entry_widget.config(font = ("Times New Roman", 13))

# кнопка для начала поиска
startButton = Button(window, text = "Начать перевод", command = buttonClicked)
startButton.grid(column = 2, row = 0, padx = 40, pady = 5)
startButton.config(font = ("Times New Roman", 11))

# лимит на 30 вводимых символов
entry_word.trace("w", lambda *args: character_limit(entry_word))

window.mainloop