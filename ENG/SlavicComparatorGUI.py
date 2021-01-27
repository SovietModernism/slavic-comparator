import SlavicComparatorAdditional as sca   # local module with functions
from tkinter import *
from ctypes import windll


# bool for checking, if there was an unsuccessful try to input a word
anErrorOnceOccured = None

# bool for checking, if anything was once translated
translatedAgain = False

# limit of 30 symbols in the string you input
def character_limit(entryWord):
    if len(entryWord.get()) > 30:
        entryWord.set(entryWord.get()[:30])


# an event when clicking a button
def buttonClicked():

    global anErrorOnceOccured
    global warningText

    try:
        sca.isEntryLatin(entryWord)
        
    except StopIteration:
            anErrorOnceOccured = True
            warningText.place(x = 50, y = 425)

    else:
        if anErrorOnceOccured:
            warningText.place_forget()
        doTranslate()


# creates empty sample labels for languages, and list them
def createLabels():

    global textVariablesList

    # creation and initialization of variables for keeping text
    L1t = StringVar()
    L1t.set("Russian: ")
    
    L2t = StringVar()
    L2t.set("Belarusian: ")

    L3t = StringVar()
    L3t.set("Russian: ")

    L4t = StringVar()
    L4t.set("Rusyn: ")

    L5t = StringVar()
    L5t.set("Old Russian: ")

    L7t = StringVar()
    L7t.set("Polish: ")

    L8t = StringVar()
    L8t.set("Kashubian: ")

    L9t = StringVar()
    L9t.set("Silesian: ")

    L10t = StringVar()
    L10t.set("Upper Sorbian: ")

    L11t = StringVar()
    L11t.set("Lower Sorbian: ")

    L12t = StringVar()
    L12t.set("Polabian: ")

    L13t = StringVar()
    L13t.set("Czech: ")

    L14t = StringVar()
    L14t.set("Slovak: ")

    L16t = StringVar()
    L16t.set("Slovenian: ")

    L17t = StringVar()
    L17t.set("Croatian: ")

    L18t = StringVar()
    L18t.set("Serbian: ")

    L19t = StringVar()
    L19t.set("Serbocroatian: ")

    L20t = StringVar()
    L20t.set("Bosnian: ")

    L21t = StringVar()
    L21t.set("Macedonian: ")

    L22t = StringVar()
    L22t.set("Bulgarian: ")

    L23t = StringVar()
    L23t.set("Church Slavonic: ")


    # creation of labels with text themselves
    L0 = Label(window, text = "EAST SLAVIC LANGUAGES")
    L1 = Label(window, textvariable = L1t)
    L2 = Label(window, textvariable = L2t)
    L3 = Label(window, textvariable = L3t)
    L4 = Label(window, textvariable = L4t)
    L5 = Label(window, textvariable = L5t)

    L6 = Label(window, text = "WEST SLAVIC LANGUAGES")
    L7 = Label(window, textvariable = L7t)
    L8 = Label(window, textvariable = L8t)
    L9 = Label(window, textvariable = L9t)
    L10 = Label(window, textvariable = L10t)
    L11 = Label(window, textvariable = L11t)
    L12 = Label(window, textvariable = L12t)
    L13 = Label(window, textvariable = L13t)
    L14 = Label(window, textvariable = L14t)

    L15 = Label(window, text = "SOUTH SLAVIC LANGUAGES")
    L16 = Label(window, textvariable = L16t)
    L17 = Label(window, textvariable = L17t)
    L18 = Label(window, textvariable = L18t)
    L19 = Label(window, textvariable = L19t)
    L20 = Label(window, textvariable = L20t)
    L21 = Label(window, textvariable = L21t)
    L22 = Label(window, textvariable = L22t)
    L23 = Label(window, textvariable = L23t)

    # listing of labels and their text variables.
    # 1st one is needed for keeping labels, 2nd - for changing their text values
    labelsPlaceList = [L0, L1, L2, L3, L4, L5, L6, L7, L8,
                      L9, L10, L11, L12, L13, L14, L15,
                      L16, L17, L18, L19, L20, L21, L22, L23]

    textVariablesList = [L1t, L2t, L3t, L4t, L5t, L7t, L8t,
                         L9t, L10t, L11t, L12t, L13t, L14t,
                         L16t, L17t, L18t, L19t, L20t, L21t, L22t, L23t]

    # placing labels on window, as well as setting their font
    a = 150    # east slavic
    b = 150    # west slavic
    c = 150    # south slavic

    for i in range(0, 24):

        labelsPlaceList[i].config(font = ("Times New Roman", 11))

        if i > 5:
            if i > 14:
                labelsPlaceList[i].place(x = 975, y = c)
                c += 25
            else:
                labelsPlaceList[i].place(x = 525, y = b)
                b += 25
        else:
            labelsPlaceList[i].place(x = 50, y = a)
            a += 25

    # separated placing of labels with language families
    labelsPlaceList[0].place(x = 50, y = 130)
    labelsPlaceList[6].place(x = 525, y = 130)
    labelsPlaceList[15].place(x = 975, y = 130)


# function that brings labels' text to default
def labelsToDefault():

    textVariablesList[1].set("Russian: ")
    textVariablesList[2].set("Belarusian: ")
    textVariablesList[3].set("Ukrainian: ")
    textVariablesList[4].set("Rusyn: ")
    textVariablesList[5].set("Old Russian: ")
    textVariablesList[6].set("Polish: ")
    textVariablesList[7].set("Kashubian: ")
    textVariablesList[8].set("Silesian: ")
    textVariablesList[9].set("Upper Sorbian: ")
    textVariablesList[10].set("Lower Sorbian: ")
    textVariablesList[11].set("Polabian: ")
    textVariablesList[12].set("Czech: ")
    textVariablesList[13].set("Slovak: ")
    textVariablesList[14].set("Slovenian: ")
    textVariablesList[15].set("Croatian: ")
    textVariablesList[16].set("Serbian: ")
    textVariablesList[17].set("Serbocroatian: ")
    textVariablesList[18].set("Bosnian: ")
    textVariablesList[19].set("Macedonian: ")
    textVariablesList[20].set("Bulgarian: ")
    textVariablesList[21].set("Church Slavonic: ")


# function that adds labels the translations
def doTranslate():

    global translatedAgain
    # returning to the default values, so
    # text won't place over itself
    if translatedAgain:
        labelsToDefault()

    translation = ""
    for i in range(0, 21):
        translation = sca.getTranslation(entryWord, sca.language[i])
        textVariablesList[i].set(textVariablesList[i].get() + translation)

    translatedAgain = True



# window options
window = Tk()
window.title("Slavic Comparator")
window.geometry('1500x475')
window.resizable(False, False)

# standartization of DPI and the size of the window for all ways of executing a program
window.call('tk', 'scaling', 1.7)
windll.shcore.SetProcessDpiAwareness(1)

# checking if there is an Internet connection, as well as if Glosbe site is online
if sca.isConnected() == "noSiteConnectionError":
    noSiteText = Label(window, text = "Server of Glosbe is working, but it returned an error code!")
    noSiteText.place(x = 25, y = 10)
    noSiteText.config(font = ("Times New Roman", 11), fg = "red")

elif sca.isConnected() == "urllib.error.URLError":
    noConnectText = Label(window, text = "This program needs an Internet connection to work (which isn't now), or Glosbe site just suddenly became inaccessible.")
    noConnectText.place(x = 25, y = 10)
    noConnectText.config(font = ("Times New Roman", 11), fg = "red")

elif sca.isConnected() == "yes":

    # initial text
    entryText = Label(window, text = "Input a word in English:")
    entryText.place(x = 575, y = 10)
    entryText.config(font = ("Times New Roman", 14))

    # string for input
    entryWord = StringVar()
    entryWidget = Entry(window, width = 40, textvariable = entryWord)
    entryWidget.place(x = 475, y = 55)
    entryWidget.config(font = ("Times New Roman", 13))

    # button for translation
    startButton = Button(window, text = "Translate", command = buttonClicked)
    startButton.place(x = 950, y = 52.5)
    startButton.config(font = ("Times New Roman", 11))

    # warning text, if input word is incorrect
    warningText = Label(window, text = "Your word contains non-Latin symbols or spaces!")
    warningText.config(font = ("Times New Roman", 12), fg = "red")
    warningText.place_forget()

    # tracking the symbol limit
    entryWord.trace("w", lambda *args: character_limit(entryWord))

    createLabels()

    window.mainloop()
