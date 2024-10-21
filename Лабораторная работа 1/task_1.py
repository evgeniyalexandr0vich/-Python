numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

number_none = 4

sum_of_numbers = sum(numbers[:number_none]) + sum(numbers[number_none + 1:])
count_of_numbers = len(numbers)
average_of_numbers = sum_of_numbers / count_of_numbers # TODO заменить значение пропущенного элемента средним арифметическим
numbers[number_none] = average_of_numbers

print("Измененный список:", numbers)
