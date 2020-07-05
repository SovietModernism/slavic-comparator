# SlavicComparator
Small program written in Python, allowing you to input a word in **English** / **Russian** and get its translations from all other Slavic languages. Translations are done with Glosbe API, GUI implemented with Tkinter.

Note that I initially started to code this project in Russian (with commits in Russian etc), eventually coming up with the idea it should be in English as well. That's why it has **two versions**, for both languages. The only difference between them is their interface and the word you input (either in Russian or English).

Now to the files and folders:

* **SlavicComparatorGUI.py** - the program's main part

* **SlavicComparatorFunctions.py** - module keeping all the functions which don't directly interact with Tkinter (only through the main part).

* **/console_version** - folder keeping console versions of the program. Might be easier to use them in terms of debug, also work faster a bit

Known (potential) bugs:

* Если в наборе данных, полученных c Glosbe API, появится ещё какое-нибудь лишнее техническое слово, то результат перевода может оказаться неправильным. Для уже известных мне "аномальных" данных есть регулярные выражения, все эти данные обрабатывающие - если появится что-то новое, то это скорее всего сразу будет заметно.

* Наличие в латинских словах (из перевода) похожих кириллических символов никак не обработано. Например, если два перевода будут отличаться лишь буквой "о" (одна из которых - латинская, а другая - кириллическая), то программа сочтёт эти два слова разными и выведет их вместе, хоть визуально они и одинаковы. Тем не менее, такой ситуации я сам ещё не встречал, в отличие от обратной (наличие латинских букв в кириллическом слове), однако вот это уже обработано.

* В консольной версии программы некоторые символы могут не отображаться. Особенно хорошо это видно на примере церковнославянских слов, которые иногда записаны глаголицей.
