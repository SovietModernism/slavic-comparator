import SlavicComparatorAdditional as sca   # локальный модуль с функциями
import urllib.error
from tkinter import *
from ctypes import windll


class App(Tk):
    
    # bool for checking, if there was an unsuccessful try to input a word
    anErrorOnceOccured = None

    # bool for checking, if anything was once translated
    translatedAgain = False

    
    # limit of 30 symbols in the string you input
    def character_limit(self, entryWord):
        if len(entryWord.get()) > 30:
            entryWord.set(entryWord.get()[:30])
                
                
    # an event when clicking a button
    def buttonClicked(self):

        try:
            sca.isEntryLatin(self.entryWord)
                
        except StopIteration:
            self.anErrorOnceOccured = True
            self.warningText.config(text = "Your word contains non-Latin symbols or spaces!")
            self.warningText.place(x = 50, y = 425)

        else:
            if self.anErrorOnceOccured:
                self.warningText.place_forget()
            self.doTranslate()
                
                
    # creates empty sample labels for languages, and list them
    def createLabels(self):

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
        L0 = Label(self, text = "EAST SLAVIC LANGUAGES")
        L1 = Label(self, textvariable = L1t)
        L2 = Label(self, textvariable = L2t)
        L3 = Label(self, textvariable = L3t)
        L4 = Label(self, textvariable = L4t)
        L5 = Label(self, textvariable = L5t)

        L6 = Label(self, text = "WEST SLAVIC LANGUAGES")
        L7 = Label(self, textvariable = L7t)
        L8 = Label(self, textvariable = L8t)
        L9 = Label(self, textvariable = L9t)
        L10 = Label(self, textvariable = L10t)
        L11 = Label(self, textvariable = L11t)
        L12 = Label(self, textvariable = L12t)
        L13 = Label(self, textvariable = L13t)
        L14 = Label(self, textvariable = L14t)

        L15 = Label(self, text = "SOUTH SLAVIC LANGUAGES")
        L16 = Label(self, textvariable = L16t)
        L17 = Label(self, textvariable = L17t)
        L18 = Label(self, textvariable = L18t)
        L19 = Label(self, textvariable = L19t)
        L20 = Label(self, textvariable = L20t)
        L21 = Label(self, textvariable = L21t)
        L22 = Label(self, textvariable = L22t)
        L23 = Label(self, textvariable = L23t)

        # listing of labels and their text variables.
        # 1st one is needed for keeping labels, 2nd - for changing their text values
        labelsPlaceList = [L0, L1, L2, L3, L4, L5, L6, L7, L8,
                      L9, L10, L11, L12, L13, L14, L15,
                      L16, L17, L18, L19, L20, L21, L22, L23]

        self.textVariablesList = [L1t, L2t, L3t, L4t, L5t, L7t, L8t,
                         L9t, L10t, L11t, L12t, L13t, L14t,
                         L16t, L17t, L18t, L19t, L20t, L21t, L22t, L23t]

        # placing labels on window, as well as setting their font
        a = 150    # east slavic
        b = 150    # west slavic
        c = 150    # south slavic

        for i in range(0, 24):

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

        # separated placing of labels with language families
        labelsPlaceList[0].place(x = 50, y = 130)
        labelsPlaceList[6].place(x = 525, y = 130)
        labelsPlaceList[15].place(x = 975, y = 130)


    # function that brings labels' text to default
    def labelsToDefault(self):

        self.textVariablesList[1].set("Russian: ")
        self.textVariablesList[2].set("Belarusian: ")
        self.textVariablesList[3].set("Ukrainian: ")
        self.textVariablesList[4].set("Rusyn: ")
        self.textVariablesList[5].set("Old Russian: ")
        self.textVariablesList[6].set("Polish: ")
        self.textVariablesList[7].set("Kashubian: ")
        self.textVariablesList[8].set("Silesian: ")
        self.textVariablesList[9].set("Upper Sorbian: ")
        self.textVariablesList[10].set("Lower Sorbian: ")
        self.textVariablesList[11].set("Polabian: ")
        self.textVariablesList[12].set("Czech: ")
        self.textVariablesList[13].set("Slovak: ")
        self.textVariablesList[14].set("Slovenian: ")
        self.textVariablesList[15].set("Croatian: ")
        self.textVariablesList[16].set("Serbian: ")
        self.textVariablesList[17].set("Serbocroatian: ")
        self.textVariablesList[18].set("Bosnian: ")
        self.textVariablesList[19].set("Macedonian: ")
        self.textVariablesList[20].set("Bulgarian: ")
        self.textVariablesList[21].set("Church Slavonic: ")


    # function that adds labels the translations
    def doTranslate(self):

        # returning to the default values, so
        # text won't place over itself
        if self.translatedAgain:
            self.labelsToDefault()

        translation = ""
        for i in range(0, 21):
            try:
                translation = sca.getTranslation(self.entryWord, sca.language[i])
                self.textVariablesList[i].set(self.textVariablesList[i].get() + translation)
                
            except urllib.error.URLError:
                self.warningText.config(text = "No Internet connection, or the Glosbe site just become inaccessible.")
                self.warningText.place(x = 50, y = 425)
                break
            
            except:
                self.warningText.config(text = "An unexpected error occured!")
                self.warningText.place(x = 50, y = 425)
                break

        self.translatedAgain = True

    
    def __init__(self): 
        super().__init__()

        # initial text
        entryText = Label(self, text = "Input a word in English:")
        entryText.place(x = 555, y = 10)
        entryText.config(font = ("Times New Roman", 14))
 
        # string for input
        self.entryWord = StringVar()
        entryWidget = Entry(self, width = 40, textvariable = self.entryWord)
        entryWidget.place(x = 475, y = 55)
        entryWidget.config(font = ("Times New Roman", 13))

        # button for translation
        startButton = Button(self, text = "Translate", command = self.buttonClicked)
        startButton.place(x = 950, y = 52.5)
        startButton.config(font = ("Times New Roman", 11))

        self.warningText = Label(self)
        self.warningText.place(x = 50, y = 425)
        self.warningText.config(font = ("Times New Roman", 12), fg = "red")
        self.warningText.place_forget()
        
        # tracking the symbol limit
        self.entryWord.trace("w", lambda *args: self.character_limit(self.entryWord))

        self.createLabels()


# GUI start
if __name__ == "__main__": 
    root = App()

    root.geometry('1500x475')
    root.resizable(False, False)

    # standartization of DPI and the size of the window for all ways of executing a program
    root.call('tk', 'scaling', 1.7)
    windll.shcore.SetProcessDpiAwareness(1)
    
    root.title("Slavic Comparator")
    
    root.mainloop()