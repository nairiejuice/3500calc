import csv

input_file = open('InputDataSample2.csv')

reader = csv.reader(input_file, delimiter=',')

for i in reader:
    print(i[0])

input_file.close()

#This is Salvador
