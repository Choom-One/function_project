import csv

child = 0
young = 0
people = 0
man = 0
old = 0


with open('homeWork.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:
        if int(row['age']) < 12:
            child += 1

        if 12 < int(row['age']) <= 18:
            young += 1

        if 18 < int(row['age']) <= 25:
            people += 1

        if 25 < int(row['age']) <= 40:
            man += 1

        if 40 < int(row['age']):
            old += 1


with open('new_file.csv', 'w', newline='') as newcsv:
    writer = csv.writer(newcsv, delimiter='-')
    writer.writerow(['chlid', child])
    writer.writerow(['young', young])
    writer.writerow(['people', people])
    writer.writerow(['man', man])
    writer.writerow(['old', old])