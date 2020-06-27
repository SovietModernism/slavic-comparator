import urllib.request
import json
import re
import os


def getTranslation(wordURL, language2):

    source = "https://iapi.glosbe.com/iapi3/wordlist?l1=ru&l2=" + language2 + \
             "&q=" + wordURL + "&after=1&includeTranslations=true"

    # в словарь собирается информация из запроса
    with urllib.request.urlopen(source) as url:
        data = json.loads(url.read().decode())

    # словарь превращается в строку, отсеиваются все слова
    data = str(data)
    parser = re.findall(r'\w+', data)

    # удаление ненужных технических слов
    parser.remove('after')
    parser.remove('phrase')
    parser.remove('translations')
    parser.remove('success')
    parser.remove('True')

    # проверка, действительно ли было переведено нужное слово, либо же что-то похожее
    if (parser[0] != word):
        return "нет информации"
    else:
        # дополнительные переводы включаются в результат, если те не совпадают с основным переводом
        if (len(parser) >= 3):
            if parser[1] != parser[2].lower():
                return parser[1] + ' / ' + parser[2]
            elif (len(parser) >= 4) and (parser[1] != parser[3].lower()):
                return parser[1] + ' / ' + parser[3]
            else:
                return parser[1]
        else:
            return parser[1]


def isFullyCyrillic(text):    # проверка на кириллическое слово и наличие пробелов
    try:

        for i in text:
            if not bool(re.search('[\u0400-\u04FF]', i)):
                raise StopIteration

    except StopIteration:
        # цикл был прерван -> есть не-кириллическая буква
        return False

    else:
        # цикл не был прерван -> слово полностью на кириллице
        return True


try:
    if (urllib.request.urlopen("https://ru.glosbe.com").getcode() != 200):   # проверка на активность сайта
        print("Сайт Glosbe, на котором основано это приложение, сейчас по какой-то причине не работает!")
        os.system("pause")

except urllib.error.URLError:
    print("Без интернета это приложение не сможет работать, а сейчас подключение отсутствует.")
    os.system("pause")

else:
    while (True):

        while(True):    # проверка слова на нормальность
            print("Введите слово на русском:")
            word = input()

            if len(word) <= 30:
                if isFullyCyrillic(word):
                    # перекодирование слова в URL-стиль для дальнейшей работы с ним
                    wordURL = urllib.parse.quote(word)
                    break
                else:
                    print("В слове присутствуют не-кириллические символы либо пробелы, попробуйте ещё раз.")
            else:
                print("Слово слишком длинное.")

        try:
            print("\nВОСТОЧНОСЛАВЯНСКИЕ ЯЗЫКИ\n")

            print("Белорусский: ", getTranslation(wordURL, 'be'))
            print("Украинский: ", getTranslation(wordURL, 'uk'))
            print("Русинский: ", getTranslation(wordURL, 'rue'))
            print("Древнерусский: ", getTranslation(wordURL, 'orv'))

            print("\nЗАПАДНОСЛАВЯНСКИЕ ЯЗЫКИ\n")

            print("Польский: ", getTranslation(wordURL, 'pl'))
            print("Кашубский: ", getTranslation(wordURL, 'csb'))
            print("Силезский: ", getTranslation(wordURL, 'szl'))
            print("Верхнелужицкий: ", getTranslation(wordURL, 'hsb'))
            print("Нижнелужицкий: ", getTranslation(wordURL, 'dsb'))
            print("Полабский: ", getTranslation(wordURL, 'pox'))
            print("Чешский: ", getTranslation(wordURL, 'cs'))
            print("Словацкий: ", getTranslation(wordURL, 'sk'))

            print("\nЮЖНОСЛАВЯНСКИЕ ЯЗЫКИ\n")

            print("Словенский: ", getTranslation(wordURL, 'sl'))
            print("Хорватский: ", getTranslation(wordURL, 'hr'))
            print("Сербский: ", getTranslation(wordURL, 'sr'))
            print("Сербохорватский: ", getTranslation(wordURL, 'sh'))
            print("Боснийский: ", getTranslation(wordURL, 'bs'))
            print("Македонский: ", getTranslation(wordURL, 'mk'))
            print("Болгарский: ", getTranslation(wordURL, 'bg'))
            print("Церковнославянский: ", getTranslation(wordURL, 'cu'))

            print("\nВыбрать новое слово? (да / любое иное слово или символ)")
            word = input()
            if (word != 'да'):
                break
            else:
                os.system('cls')

        # возникает при работе функции getTranslation на этапе удаления ненужных слов, если их вдруг не окажется
        except ValueError:
            print("Произошла ошибка при обработке нестандартных полученных данных.")
            os.system("pause")
            break

        # возникает когда urllib пытается работать с каким-либо сайтом, но интернета нет
        except urllib.error.URLError:
            print("Во время выполнения программы пропало подключение к интернету")
            os.system("pause")
            break

        # ловит все остальные ошибки
        except:
            print("Произошла непредвиденная ошибка.")
            os.system("pause")
            break
