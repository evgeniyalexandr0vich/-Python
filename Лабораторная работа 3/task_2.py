# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, sep=","):
    first = first_group.split(sep)
    second = second_group.split(sep)
    intersection_participants = list(set(first).intersection(second))
    intersection_participants.sort()
    return intersection_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))
