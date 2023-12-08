import csv
from csv import DictReader

from example_from_lesson.test_data.read_write_files.files import CSV_FILE

with open(CSV_FILE, newline='') as f:
    reader = csv.reader(f)

    # Извлекаем заголовок
    header = next(reader)

    # Итерируемся по данным делая из них словари
    for row in reader:
        print(row)
       # print(dict(zip(header, row)))

print(100 * "+")

with open(CSV_FILE, newline='') as f:
    reader = DictReader(f)

    # Итерируемся по данным делая из них словари
    for row in reader:
        print(row)

