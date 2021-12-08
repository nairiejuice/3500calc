# NAME: Salvador Vargas, Samuel Kaing, Wesley Tam
# ASGT: Class Project
# ORGN: CSUB - CMPS 3500
# FILE: calc.py
# DATE: Fall 2021
# PYTHON IMPLEMENTATION OF A CUSTOM STATISTICS SUMMARY CALCULATOR
# NEW COMMENT *TEST*

import csv

print("\nPlease wait while the program executes...")

try:
    def search_boston_lists(boston_lists, input, column_name):
        total_count = 0
        column_num = 0
        match = []
        names = ["Column1", "Column2", "Column3", "Column4", "Column5",
                 "Column6", "Column7", "Column8", "DataSet"]

        for i in range(len(names)):
            if names[i] == column_name:
                column_num = i + 1

        if (column_num < 9):
            for row in range(len(boston_lists[int(column_num)])):
                if boston_lists[int(column_num)][row] == str(input):
                    total_count += 1
                    match.append([input, column_num, row + 1])
            print(input, "is present", str(total_count),
                  "times in column", str(column_num))

        elif (column_num == 9):
            for column in range(len(boston_lists)):
                for row in range(len(boston_lists[int(column)])):
                    if boston_lists[int(column)][row] == str(input):
                        total_count += 1
                        match.append([input, int(column) + 1, row + 1])
            print(input, "is present", str(
                total_count), "times in the data set")

        elif (column_num == 0):
            print("Error: No such column exists for search_boston_lists")

        print()
        print("Details:")
        print("*********************************")
        print()

        for i in match:
            print(i[0], "is present in Column", i[1], "row", i[2])
except ValueError:
    print("\nPlease give a column number within range\n")


def clean(boston_lists):
    temp = []

    for i in range(len(boston_lists)):
        if boston_lists[i][0] != '':
            temp.append(boston_lists[i])

    return temp

###########################################################


def readCSV():
    # declares two empty lists of data
    listA = []
    listB = []
    # opens file to read with 'r'
    # 'with' allows opening and processing of file contents without
    # the need to call a close()
    # here we are assigning csv file to variable 'f'
    try:
        with open('InputDataSample.csv', 'r') as f:
            # iterates over file line by line
            # i is the line number (index) start from 0
            # enumerate returns each value along with its corresponding index
            for index, line in enumerate(f):
                # skips over header line
                if index > 0:
                    # every time a ',' is found
                    # .split creates a new line
                    x = line.split(',')
                    # appends columns to lists
                    listA.append(int(x[0]))
                    listB.append(int(x[1]))
        # returns lists
        return listA, listB
    except FileNotFoundError:
        print("\nPlease provide a valid file for the statistics calculator\n")
    except IOError:
        print("\nCorrupted file, please provide one that works\n")


# calls function readCSV
readCSV()

# 'dataSet' set equal to csv file
dataSet = 'InputDataSample.csv'

try:
    # returns length of data
    def count(dataSet):
        return len(dataSet)

    # returns unique values from data in string format
    def unique(dataSet):
        return len((set(dataSet)))

    # returns mean
    def mean(dataSet):
        return round(sum(dataSet) / len(dataSet))

    # returns median
    def median(dataSet):
        n = len(dataSet)
        dataSet.sort()
        if n % 2 == 0:
            # median for odd length data
            median1 = dataSet[n//2]
            # median for even length data
            median2 = dataSet[n//2 - 1]
            median = round((median1 + median2)/2)
        else:
            median = round(dataSet[n//2])
        return median

    # returns mode
    def mode(dataSet):
        # creating a dictionary called 'frequency'
        frequency = {}
        # looping through list recording frequency
        # of each value
        for number in dataSet:
            frequency.setdefault(number, 0)
            frequency[number] += 1
        # converting values into list using
        # python built-in '.values()' function
        # we have multiple values that appear an
        # equal number of times, therefore we have several modes
        # now creating a list of those values
        highestFrequency = max(frequency.values())
        highestFreqLst = []
        for number, freq in frequency.items():
            if freq == highestFrequency:
                highestFreqLst.append(number)
        # mode is any number that appears twice in this case
        # returning the largest number that appears twice
        # in order to only return a single value
        return(max(highestFreqLst))

    # returns variance
    def variance(dataSet):
        # number of observations
        n = len(dataSet)
        # mean of the data
        mean = sum(dataSet) / n
        # square deviations
        deviations = [(x - mean) ** 2 for x in dataSet]
        # variance
        variance = round(sum(deviations) / n)
        return variance

    # returns standard deviation
    def stddev(dataSet):
        return round(variance(dataSet)**0.5)

    # returns minimum value from data
    def minimum(dataSet):
        return min(dataSet)

    # returns maximum value from data
    def maximum(dataSet):
        return max(dataSet)

    # each percentile calculation values
    percentile_values = [20, 40, 50, 60, 80]

    # each percentile calculation values
    def percentile(dataSet, percentile_values):
        # returns percentile value from data
        # sort data then calculate
        length = len(dataSet)
        p = (length * percentile_values) / 100
        return sorted(dataSet)[int(p)]
except TimeoutError:
    print("\nData processing took too long\n")
except ZeroDivisionError:
    print("\nCan not divide by zero, provide a different data set\n")

###########################################################
# Main for data processing

boston_lists = [[], [], [], [], [], [], [], [], [], [], [], [], []]
try:
    with open('Boston_Lyft_Uber_Data.csv', 'r') as boston_data:
        data = []

        for idx, line in enumerate(boston_data):
            if idx > 0 and 'NA' not in line:
                data.append(line)
        data = list(dict.fromkeys(data))

        for idx, line in enumerate(data):
            # Skips row with column names
            words = line.split(',')

            # Delete all strings in words[] before appending
            for j, value in enumerate(words):
                if not value.replace('.', '', 1).strip().isdigit():
                    words[j] = ''

            for i in range(len(boston_lists)):
                boston_lists[i].append(words[i].strip())

        boston_lists = clean(boston_lists)

        print("\nPlease give a command to search either a column by name")
        print("or the entire dataset.")
        print("\nExample: Search 3, Column1")
        print("Example: Search 2, DataSet")
        print("\nCommands in any other format will not be valid!")

        search_number, search_column = input("\nSearch ").split(", ")
        search_boston_lists(boston_lists, search_number, search_column)
        print('')

        boston_data.close()
except FileNotFoundError:
    print("\nPlease provide a valid file for the search function\n")
except IOError:
    print("\nCorrupted file\n")
except TimeoutError:
    print("\nData processing took too long\n")
###########################################################
# Main for calculator

# declares top row
topRow = ['Descriptor', 'Column A', 'Column B']
# inserts "*" between rows
spacer = ['**********', '********', '********']
# declares labels
labels = ['Count', "Unique", 'Mean', 'Median', 'Mode', 'SD',
          'Variance', 'Minimum', 'P20', 'P40',
          'P50', 'P60', 'P80',
          'Maximum']
# declares value function list
valueFunctions = [count, unique, mean, median, mode, stddev,
                  variance, minimum, percentile, percentile,
                  percentile, percentile, percentile, maximum]

# calls function to read csv file function
listA, listB = readCSV()

# returns data in format
# '20' is space between columns
# '3' is number of columns
# without '>' numbers are aligned to the right
# '<' aligns to the left
# '^' centers the text
# this is known as 'padding'
# {} have to be used with .format
rowFormat = "{:>20}" * 3
# .format() interpolates methods into pre-built strings
# displays formatted header
# '*' is an unpacking operator that unpacks iterable values in python
print(rowFormat.format(*topRow))
# displays formatted "*" between rows
print(rowFormat.format(*spacer))
# iterates over 'labels' list
# 'i' is assigned an index number, starting with 0
# dscrptr returns the string in 'labels'
for i, dscrptr in enumerate(labels):
    # each row
    calc_row = [dscrptr]
    # special formatting case for indices 8 - 12
    if 12 >= i >= 8:
        # i starts at 8, subtract 8 to start at beginning
        # of percentile_values list with index 0
        calc_row += [valueFunctions[i](listA, percentile_values[i-8])]
        calc_row += [valueFunctions[i](listB, percentile_values[i-8])]
        # formatting of all other indices
        # transferring values of 'listA', 'listB' to 'valueFunctions'
        # and then to 'calc_row' for display purposes
        # transferring values to 'valueFunctions' to iterate through
        # that list
    else:
        calc_row += [valueFunctions[i](listA)]
        calc_row += [valueFunctions[i](listB)]
    # print all 'row's
    print(rowFormat.format(*calc_row))
