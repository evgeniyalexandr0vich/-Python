# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []
    with open(INPUT_FILENAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
        # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, 'w') as g:
        json_data = json.dumps(data, indent=4)
        return g.write(json_data)
        # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
