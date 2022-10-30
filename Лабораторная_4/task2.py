def get_count_char(str_):
    for letter in str_:
        if letter.isalpha() == True:
            letters = ""
            letters += letter
            dicta[letter] = str_.count(letter)
    return dicta

def percent(dicta):
    suma = sum(dicta.values())
    for key, value in dicta.items():
        dicta[key] = round(value / suma * 100, 2)
    return dicta

dicta = {}
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
""".lower()
print(get_count_char(main_str))
