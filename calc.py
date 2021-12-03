import csv

# def non_numerical(boston_lists):
#     numerical_boston_lists = []
#     for column in range(len(boston_lists)):
#         if (boston_lists[column][0].replace('.', '', 1).isdigit()):
#             numerical_boston_lists.append(boston_lists[column])
#     return numerical_boston_lists 
# def missing_or_empty_values(boston_lists):
#     for column in range(len(boston_lists)):
#         for row in range(len(boston_lists[0])):
#             if boston_lists[column][row] == 'NA' or boston_lists[column][row] == '':
#                 for column in range(len(boston_lists)):
#                     boston_lists[column].pop(row)
#     #Get length of list inside boston_lists
#     #print ("missing values function")
def search_boston_lists(boston_lists, input, column_name):
    total_count = 0
    match = []
    "Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7", "Column8", "DataSet"
    if (column_name == "Column1"): column_num = 1
    elif (column_name == "Column2"): column_num = 2
    elif (column_name == "Column3"): column_num = 3
    elif (column_name == "Column4"): column_num = 4
    elif (column_name == "Column5"): column_num = 5
    elif (column_name == "Column6"): column_num = 6
    elif (column_name == "Column7"): column_num = 7
    elif (column_name == "Column8"): column_num = 8
    elif (column_name == "DataSet"): column_num = 9
    else:
        print("Error: No such column exists for search_boston_lists")
    if (column_num != 9):
        for row in range(len(boston_lists[int(column_num)])):
            if boston_lists[int(column_num)][row] == str(input):
                total_count += 1
                match.append([input, column_num, row + 1])
        print(input, "is present", str(total_count), "times in column", str(column_num))
    elif (column_num == 9):
        for column in range(len(boston_lists)):
            for row in range(len(boston_lists[int(column)])):
                if boston_lists[int(column)][row] == str(input):
                    total_count += 1
                    match.append([input, int(column), row + 1])
        print(input, "is present", str(total_count), "times in the data set") 
    print()
    print("Details:")
    print("*********************************")
    print()
    for i in match:
        print(i[0], "is present in Column", i[1], "row", i[2])
# #This is the beginning of main
# input_data_file = open('InputDataSample2.csv')
# reader_input_data = list(csv.reader(input_data_file, delimiter=','))
# # testing proper loading of reader_input_data
# # for i in reader_input_data:
# #     print(i[0])
# #     print(i[1])
# # count(reader_input_data)
# # unique(reader_input_data)
# boston_id = []
# datetime = []
# timezone = []
# cab_type = []
# product_id = []
# price = []
# distance = []
# humidity = []
# windSpeed = []
# windGust = []
# windGustTime = []
# visibility = []
# temperatureHigh = []
# boston_lists = [boston_id, datetime, timezone, cab_type, product_id, price, 
# distance, humidity, windSpeed,windGust, windGustTime, visibility, temperatureHigh]
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
#with open('Boston_Lyft_Uber_Data3.csv', 'r') as boston_data:
#    for idx, line in enumerate(boston_data):
#        if idx > 0:
#            words = line.split(',')
#            for i in range(len(boston_lists)):
#                if words[i] in boston_lists[0]:
#                    break
#                else:
#                    boston_lists[i].append(words[i].strip())

with open('Boston_Lyft_Uber_Data5.csv', 'r') as boston_data:
    for idx, line in enumerate(boston_data):
        # Skips row with column names
        if idx > 0:
            words = line.split(',')

            #Handles '' or 'NA'
            NA_count = words.count('NA')
            empty_count = words.count('')
            
            #Handles Duplicates
            duplicate = False
            if words[0] in boston_lists[0]:
                duplicate = True

            # Delete all strings in words[] before appending
            for j, value in enumerate(words):
                if not value.replace('.', '', 1).isdigit():
                    words
                    # Deletes column only on first loop of csv

            if (NA_count == 0 and empty_count == 0 and not duplicate):
                for i in range(len(boston_lists)):

                    # Index error Here
                    # Figure out how to make boston_lists a dynamic size
                    # By popping, words[] goes out of range
                    boston_lists[i].append(words[i].strip())

# x = [[] for i in range(13)]
# print(boston_lists)
missing_or_empty_values(boston_lists)
# print(boston_lists)
boston_lists = non_numerical(boston_lists)
print(boston_lists)
search_number, search_column = input("Search ").split(", ")
search_boston_lists(boston_lists, search_number, search_column)
# search_boston_lists(boston_lists, 1.08, "Column1")
input_data_file.close()
boston_data.close()