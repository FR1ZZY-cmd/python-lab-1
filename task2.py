# TODO Напишите функцию find_common_participants

def find_common_participants(first_str, second_str, divider = ','):
    first_list = first_str.split(divider)
    second_list = second_str.split(divider)

    merged_list = list(set(first_list) & set(second_list))

    return sorted(merged_list)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group,participants_second_group,'|')
