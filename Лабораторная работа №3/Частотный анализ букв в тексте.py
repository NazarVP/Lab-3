# TODO  Напишите функцию count_letters
# TODO Напишите функцию calculate_frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

def count_letters(a):
    symb_dict = {}
    a_word = a.lower()
    DEFAULT_COUNT = 0
    for symb in a_word:
        if symb in a_word and symb.isalpha() == True:
            symb_dict[symb] = symb_dict.get(symb, DEFAULT_COUNT) + 1
    return symb_dict

def calculate_frequency(a):
    letter_serch = a
    letter_total = sum(a.values())
    for symb in letter_serch:
        letter_serch[symb] /= letter_total
    return letter_serch

letter_num = count_letters(main_str)
 # print(letter_num) Почему если я вывожу здесь letter_num, получаю количество символов? А если ниже...
letter_seq = calculate_frequency(letter_num)
 # print(letter_num) ... тут. То получаю уже частоту, хотя вывожу одну и ту же переменную. Что у меня перезаписывает ее?
for key, value in letter_seq.items():
    print(key, "%.2f"%value)
 # TODO Распечатайте в столбик букву и её частоту в тексте
