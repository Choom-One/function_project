import csv
import statistics


def main():
    with open('weather.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        column = {key: [] for key in reader.fieldnames}
        for row in reader:
            if row['city'] == 'Minsk':
                for key in reader.fieldnames:
                    column[key].append(row[key])
        print('degrees Average =', statistics.mean(map(float, column['degrees'])))
        print('w_speed Average =', statistics.mean(map(float, column['w_speed'])))



if __name__ == '__main__':
    main()







