import csv
from csv import DictWriter

from example_from_lesson.test_data.read_write_files.files import CSV_FILE_W

with open(CSV_FILE_W, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')

    writer.writerow(['data', 'result', 'code'])
    for i in range(10):
        writer.writerow([i, i * 100, str(bin(i))])


print(100 * "+")

with open(CSV_FILE_W, 'w', newline='') as f:
    fieldnames = ['data', 'result', 'code']
    writer = DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(10):
        row = zip(fieldnames, [i, i * 100, str(bin(i))])
        writer.writerow(dict(row))
