import csv


with open('positive.csv', 'r') as f: 
    csv_reader = csv.reader(f)
    for row in csv_reader:
        print(row)
   