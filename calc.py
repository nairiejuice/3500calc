import csv

#These are the calculator functions
#Count function done by Wesley
#The count function returns the count of numbers in columns A and B
def count(reader_input_data):
    #a_count and b_count hold the counts of their respective columns
    a_count = 0
    b_count = 0
    #Iterate through both columns in InputDataSample.csv, without the "Column A" and
    # "Column B" identifiers
    for count_data in reader_input_data[1:len(reader_input_data)]:
        #For each number in that column, increment the count by 1
        if count_data[0]:
            a_count += 1
        if count_data[1]:
            b_count += 1
    #Displays the count to the user
    print("A count:", a_count)
    print("B count:", b_count)
    
#Unique function done by Salvador
def unique(reader_input_data):
    print("This is the unique function")
    list_of_unique_numbers = []
    
    unique_numbers = set(reader_input_data)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers

print(unique(reader_input_data))

#Mean function done by Wesley
def mean(reader_input_data):
    #a_mean holds mean, a_mean_sum holds the sum of numbers in column a,
    # a_mean_count holds the count of numbers in column a, and the b counterparts
    # hold their respective values
    a_mean, b_mean = 0, 0
    a_mean_sum, b_mean_sum = 0, 0
    a_mean_count, b_mean_count = 0, 0
    #Iterate through both columns in InputDataSample.csv, without the "Column A" and
    # "Column B" identifiers
    for mean_data in reader_input_data[1:len(reader_input_data)]:
        #mean_data[0] is column a
        if mean_data[0]:
            a_mean_sum += int(mean_data[0])
            a_mean_count += 1
        if mean_data[1]:
            b_mean_sum += int(mean_data[1])
            b_mean_count += 1
    #Defintion of mean
    a_mean = a_mean_sum / a_mean_count
    b_mean = b_mean_sum / b_mean_count
    #Return the mean, rounded to a whole number
    print("A mean:", round(a_mean))
    print("B mean:", round(b_mean))

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
