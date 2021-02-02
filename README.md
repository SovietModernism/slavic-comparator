# SlavicComparator (EN)
Translations are done with **Glosbe API**, GUI implemented with **Tkinter**.

**N.B.**: I initially started to work on this project in Russian (with comments in Russian e.g.), eventually coming up with the idea it should be in English as well. That's why it has **two versions**, for both languages. The only difference between them is their interface and the word you input (either in Russian or English).

Now to the files and folders:

* **SlavicComparatorGUI.py** — program's main part

* **SlavicComparatorAdditional.py** — module keeping all the stuff which doesn't directly interact with Tkinter (only through the main part)

* **/console_version** — folder keeping console versions of the program. Might be easier to use them in terms of debug, also work a bit faster

Known (potential) bugs:

* From **Glosbe API** a dataset obtained, which not only contains translations, but unnecessary technical words and symbols as well. Of course I wrote regular expressions in order to get only the data needed... but let's imagine some **new** technicall stuff suddenly appears — an error will occure then. Or the translation results will be just incorrect, at best. However, a chance it will even happen ("garbage" magically appears from nowhere) is extremely small.

* Another one related to datasets — program consider same-looking letters different, if they belong to different alphabets (such as Latin and Cyrillic, sharing some common letters). The problem is, this program checks if translations (within one language) are even different, so you won't see the same word repeating multiple times in one single string. And it would work correctly, but Cyrillic words from Glosbe may randomly have similar-looking Latin letters inside, and the opposite (though both are rare to happen). As the result you get strings like "вада / вaда" ("water" in Belorussian), because of different "a"-s in it, even though these words look the same. Or, the only difference between 2 words might be some diacritics (like "o" and "ó") — it's another incorrect thing to appear. Unfortunately, I don't even know what could I do with it: in the 1st case, you won't be able to check if the whole word is in Latin or Cyrillic, like I did it with the word you input — Slavic languages mostly use extended Latin / Cyrillic alphabets, or even both at the same time. And in the 2nd case, you won't check it for sure, if 2 words are the same or not.

* If the Internet connection suddenly disappears while the program is running (at the stage of getting translations), the program will hang. I still haven't figured out how this could be handled (by preventing the hang and displaying an error message). Nevertheless, when reconnecting to the Internet, the program continues to work.

* In the console version of the program, some characters may not be displayed correctly. This is especially true for Church Slavonic words, being written in Glagolitic script sometimes.

___

# Slavic Comparator (RU)

Переводы выполняются с помощью **API** сайта **Glosbe**, GUI написано на **Tkinter**.

**Важно**: первоначально я работал над этим проектом на русском языке, но в конце концов пришёл к выводу, что стоит также перевести это всё и на английский. Вот почему здесь **две версии**, для обоих языков. Единственная разница между ними лишь в интерфейсе программы, языке комментариев в коде, а также во вводимом слове (русском и английском соответственно).

Теперь про файлы и папки:

* **SlavicComparatorGUI.py** — главная часть программы, по совместительству также отвечающая за графическую составляющую

* **SlavicComparatorAdditional.py** — модуль, в который было вынесено всё, что не взаимодействует с Tkinter'ом напрямую (только через файл с GUI)

* **/console_version** — папка, хранящая консольные версии программы соответственно. С помощью них может быть проще проводить debug, да и работают они немного быстрее

Известные (возможные) ошибки:

* Как уже было сказано, все переводы получаются с сайта **Glosbe** в виде строки с данными, среди которых, тем не менее, довольно много всяких ненужных слов и символов. Конечно, я написал регулярные выражения, которые бы из этого всего "доставали" только нужные данные, однако... всегда может появиться ещё какое-нибудь лишнее техническое слово, и обработано оно скорее всего не будет. А это приведёт к неправильным переводам, в лучшем случае. Впрочем, шанс, что подобный "мусор" вдруг появится из ниоткуда, крайне мал. И даже если это случится, такое будет сразу заметно.

* Ещё одна вещь, касающаяся переводов — программа вполне логично будет считать одинаково выглядящие буквы разными, если они принадлежат к разным алфавитам (пример: кириллическая и латинская "о"). Проблема в том, что программа также проверяет, одинаковы ли переводы (в пределах одного языка), поэтому, например, вы не увидите в одной и той же строке два одинаковых слова, различающихся регистром букв... И это работало бы хорошо, однако порой в кириллических словах с Glosbe встречаются латинские буквы, и наоборот. В итоге вы получаете переводы в стиле "вада / вaда" ("вода" в белорусском), различающиеся лишь буквами "а" из разных алфавитов. Либо же, единственной разницей между 2-мя словами может быть какая-нибудь диакритика (как "o" и "ó") — это тоже обычно неверно, так как выводятся почти одинаковые слова. К сожалению, я даже не знаю, что с этим можно сделать: в 1-м случае просто нельзя проверить, полностью ли слово записано в кириллице или латинице (как я делал это со словом, которое вводит пользователь) — славянские языки используют расширенные латинские и кириллические алфавиты, а то и оба в одно и то же время. Во втором же случае также не представляется возможным проверить, действительно ли слова отличаются и диакритика тут нужна, или нет.

* Если уже во время работы программы (на этапе получения переводов) внезапно исчезнет интернет, то программа зависнет. Я так и не придумал, как это можно было бы обработать, предотвратив зависание и выводя сообщение об ошибке. Тем не менее, при переподключении к интернету программа продолжает свою работу.

* Консольная версия программы не поддерживает вывод некоторых символов, и поэтому может показывать их неправильно (если вообще будет показывать). Это особенно заметно на примере церковнославянских слов, которые иногда бывают записаны глаголицей.
