import csv

#These are the calculator functions
#Count function done by Wesley
#The count function returns the count of numbers in columns A and B
def count(reader_input_data):
    #We start the counts at -1 because we don't want to count the strings "Column A"
    # and "Column B" in InputDataSample.csv
    a_count = -1
    b_count = -1
    #Iterate through both columns in InputDataSample.csv
    for count_data in reader_input_data:
        #For each number in that column, increment the count by 1
        if count_data[0]:
            a_count += 1
        if count_data[1]:
            b_count += 1
    #Displays the count to the user
    print("A count: ", a_count)
    print("B count: ", b_count)
    
#Unique function done by Salvador
def unique(reader_input_data):
    print("This is the unique function")
    list_of_unique_numbers = []
    
    unique_numbers = set(reader_input_data)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers

print(unique(reader_input_data))

# def mean():
# def median():
# def mode():
# def standard_deviation():
# def variance():
# def minimum():
# def p20():
# def p40():
# def p50():
# def p60():
# def p80():
# def maximum():

#This is the beginning of main
input_data_file = open('InputDataSample2.csv')
reader_input_data = list(csv.reader(input_data_file, delimiter=','))
#testing proper loading of reader_input_data
for i in reader_input_data:
    print(i[0])
    print(i[1])

count(reader_input_data)
unique(reader_input_data)

input_data_file.close()