# SlavicComparator
Small program written in Python, allowing you to input a word in **English** / **Russian** and get its translations from all other Slavic languages. Translations are done with **Glosbe API**, GUI implemented with **Tkinter**.

**N.B.**: I initially started to work on this project in Russian (with comments in Russian e.g.), eventually coming up with the idea it should be in English as well. That's why it has **two versions**, for both languages. The only difference between them is their interface and the word you input (either in Russian or English).

Now to the files and folders:

* **SlavicComparatorGUI.py** — program's main part

* **SlavicComparatorFunctions.py** — module keeping all the functions which don't directly interact with Tkinter (only through the main part)

* **/console_version** — folder keeping console versions of the program. Might be easier to use them in terms of debug, also work a bit faster

* **/exe_binaries** — folder keeping executable files if you need them to work without Python interpreter. I compiled it all in advance via cx_Freeze

Known (potential) bugs:

* From **Glosbe API** a dataset obtained, which not only contains translations, but unnecessary technical words and symbols as well. Of course I wrote regular expressions in order to get only the data needed... but let's imagine some **new** technicall stuff suddenly appears — an error will occure then. Or the translation results will be just incorrect, at best. However, a chance it will even happen ("garbage" magically appears from nowhere) is extremely small.

* Another one related to datasets — program consider same-looking letters different, if they belong to different alphabets (such as Latin and Cyrillic, sharing some common letters). The problem is, this program checks if translations (within one language) are even different, so you won't see the same word repeating multiple times in one single string. And it would work correctly, but Cyrillic words from Glosbe may randomly have similar-looking Latin letters inside, and the opposite (though both are rare to happen). As the result you get strings like "вада / вaда" ("water" in Belorussian), because of different "a"-s in it, though these words look the same. Or, the only difference between 2 words might be some diacritics (like "o" and "ó") — it's another incorrect thing to appear. Unfortunately, I don't even know what could I do with it: in the 1st case, you won't be able to check if the whole word is in Latin or Cyrillic, like I did it with the word you input — Slavic languages mostly use extended Latin / Cyrillic alphabets, or even both at the same time. And in the 2nd case, you won't check it for sure, if 2 words are the same or not.

* In the console version of the program, some characters may not be displayed correctly. This is especially true for Church Slavonic words, being written in Glagolitic script sometimes.
