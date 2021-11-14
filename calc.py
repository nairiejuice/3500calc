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
# def unique(reader_input_data):
#     print("This is the unique function")
#     list_of_unique_numbers = []
#     unique_numbers = set(reader_input_data)
#     for number in unique_numbers:
#         list_of_unique_numbers.append(number)
#     return list_of_unique_numbers
# print(unique(reader_input_data))
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

def non_numerical(boston_lists):
    print ("non-numerical function")
    numerical_boston_lists = []
    for column in range(len(boston_lists)):
        # result = isinstance(boston_lists[column][0], complex)
        # print(result)
        # int(value)
        #print(boston_lists[column][0])
        #print(boston_lists[column][0].replace('.', '', 1).isdigit())
        if (boston_lists[column][0].replace('.', '', 1).isdigit()):
            #print("hello")
            #boston_lists.pop(column)
            numerical_boston_lists.append(boston_lists[column])
        #print(boston_lists[column])
        #for row in range(len(boston_lists[0])):
        #    if (not isinstance(boston_lists[column][row], int)) or (not isinstance(boston_lists[column][row], float)) or (not isinstance(boston_lists[column][row], complex)):
        #        boston_lists.pop(column)
        #        break
    return numerical_boston_lists       

def missing_or_empty_values(boston_lists):
    print ("missing values function")
    for column in range(len(boston_lists)):
        for row in range(len(boston_lists[0])):
            if boston_lists[column][row] == 'NA' or boston_lists[column][row] == '':
                for column in range(len(boston_lists)):
                    boston_lists[column].pop(row)

    #Get length of list inside boston_lists

def search_boston_lists(boston_lists, input, column):
    print ("search values function")
    count = 0
    # "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7", "Column8", "DataSet"
    if (column == "Column1"):
    elif (column == "Column2"):
    elif (column == "Column3"):
    elif (column == "Column4"):
    elif (column == "Column5"):
    elif (column == "Column6"):
    elif (column == "Column7"):
    elif (column == "Column8"):
    else:
        print("Error: No such column exists for search_boston_lists")

    for row in range(len(boston_lists[int(column)])):
        if boston_lists[int(column)][row] == str(input):
            print (input, " is present 12 times in column ", column, " row ", row)
            count += 1



#This is the beginning of main
input_data_file = open('InputDataSample2.csv')
reader_input_data = list(csv.reader(input_data_file, delimiter=','))
# testing proper loading of reader_input_data
# for i in reader_input_data:
#     print(i[0])
#     print(i[1])
# count(reader_input_data)
# unique(reader_input_data)
boston_id = []
datetime = []
timezone = []
cab_type = []
product_id = []
price = []
distance = []
humidity = []
windSpeed = []
windGust = []
windGustTime = []
visibility = []
temperatureHigh = []
boston_lists = [boston_id, datetime, timezone, cab_type, product_id, price, 
distance, humidity, windSpeed,windGust, windGustTime, visibility, temperatureHigh]
# Data Cleaning: Your program should be able to perform the follwing cleaning tasks:
# ----- Load the csv file and stored into an array or data frame
# ----- Eliminate columns with non-numerical data
# ----- Eliminate all rows with missing values in any of the columns
# ----- Eliminate all rows with empty values on any of the columns
# ----- Eliminate all rows with duplicated values
# ----- Eliminate all empty rows.

# Searching capability: Your program should have an option search any element in a given column or in the entire data set.
# Example: Search in column
# $ Search(25, "Column1")
# 25 is present 12 times in column Column1.
# Details:
#     *********************************
#     25 is present in Column 1 row 25
#     25 is present in Column 1 row 365
#     .
#     .
#     .
# Example: Search in data set
# $ Search(25, "DataSet")
# 25 is present 31 times in the data set.
# Details:
#     *********************************
#     25 is present in Column 1 row 25
#     25 is present in Column 1 row 365
#     .
#     .
#     25 is present in Column 2 row 1182
#     .
#     .
#     .

with open('Boston_Lyft_Uber_Data2.csv', 'r') as boston_data:
    for idx, line in enumerate(boston_data):
        if idx > 0:
            words = line.split(',')
            for i in range(len(boston_lists)):
                if words[i] in boston_lists[0]:
                    break
                else:
                    boston_lists[i].append(words[i].strip())

# x = [[] for i in range(13)]
# print(boston_lists)
missing_or_empty_values(boston_lists)
# print(boston_lists)
boston_lists = non_numerical(boston_lists)
print(boston_lists)
search_boston_lists(boston_lists, 1.08, "1")

input_data_file.close()
boston_data.close()
