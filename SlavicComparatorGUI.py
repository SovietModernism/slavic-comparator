from tkinter import *


# лимит на вводимое слово в 30 символов
def character_limit(entry_text):
    if len(entry_text.get()) > 30:
        entry_text.set(entry_text.get()[:30])

# настройки окна
window = Tk()
window.title("Slavic Comparator")
window.geometry('1000x500')

# текст
entryText = Label(window, text = "Введите слово на русском: ", font = ("Times New Roman", 13))
entryText.grid(column = 0, row = 0)

# строка с вводом
entry_word = StringVar()    # переменная с текстом, введённым в виджет
entry_widget = Entry(window, width = 40, textvariable = entry_word)
entry_widget.grid(column = 1, row = 0)
entry_widget.config(font = ("Times New Roman", 13))

# кнопка для начала поиска
startButton = Button(window, text = "Начать перевод")
startButton.grid(column = 2, row = 0)
startButton.config(font = ("Times New Roman", 11))

# лимит на символы
entry_word.trace("w", lambda *args: character_limit(entry_word))

window.mainloop