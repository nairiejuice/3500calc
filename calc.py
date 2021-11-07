import csv

input_file = open('InputDataSample2.csv')

reader = csv.reader(input_file, delimiter=',')

#This is Sam letss gooo
#This is Sal letss gooo
#Sal trying another push

for i in reader:
    print(i[0])

input_file.close()

#making sure I can still push 
