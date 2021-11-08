import csv

#These are the calculator functions
def count(reader_input_data):
    a_count = 0
    b_count = 0
    for count_data in reader_input_data[1:-1]:
        if count_data[0]:
            print(count_data[0])
            a_count += 1
        if count_data[1]:
            b_count += 1
    print("A count: ", a_count)
    print("B count: ", b_count)

# def mean(reader_input_data):
#     print("this is mean function")
#     a_mean = 0
#     b_mean = 0
#     for mean_data in reader_input_data:
#         a_mean += mean_data[0]
#     print("A mean: ", a_mean)

    
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

count(reader_input_data)
#mean(reader_input_data)

input_data_file.close()
