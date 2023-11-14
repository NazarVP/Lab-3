# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def add_func(a, b):
    common = []
    a_list = a.split("|")
    b_list = b.split("|")
    for group in a_list:
        if group in b_list:
            common.append(group)
    return common
print(sorted(add_func(participants_second_group,participants_first_group)))
    # TODO Провеьте работу функции с разделителем отличным от запятой
