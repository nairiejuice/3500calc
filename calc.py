# NAME: Salvador Vargas, Samuel Kaing, Wesley Tam
# ASGT: Class Project
# ORGN: CSUB - CMPS 3500
# FILE: calc.py
# DATE: Fall 2021
# PYTHON IMPLEMENTATION OF A CUSTOM STATISTICS SUMMARY CALCULATOR

import sys
import csv

print("\nPlease wait while the program executes...")

# takes the list and the users input (search number) column name (column to search)
def search_boston_lists(boston_lists, input, column_name):
    # declares variables
    total_count = 0
    column_num = 0
    match = []
    names = ["Column1", "Column2", "Column3", "Column4", "Column5",
            "Column6", "Column7", "Column8", "Column9", "Column10"]

    # Changes column_name into numerical value
    for i in range(len(names)):
        # No need to do this if user entered "DataSet", break loop
        if column_name == "DataSet":
            break
        if names[i] == column_name:
            column_num = i
    
    # If user's column_name input is in valid form from names list, try searching
    if (column_name in names):
        # Throws error if column_name doesn't exist in dataset
        try:
            for row in range(len(boston_lists[int(column_num)])):
                # If value is found, increment count and append its location to match list
                if boston_lists[int(column_num)][row] == str(input):
                    total_count += 1
                    match.append([input, column_num + 1, row + 1])
            print(input, "is present", str(total_count),
                "times in column", str(column_num + 1))
        except IndexError:
            print(column_name, "does not exist in dataset")

    # column_name == "DataSet" would find all occurrences in the whole file instead
    elif (column_name == "DataSet"):
        for column in range(len(boston_lists)):
            for row in range(len(boston_lists[int(column)])):
                # If value is found, add 1 to the total count and append its found location to the output
                if boston_lists[int(column)][row] == str(input):
                    total_count += 1
                    match.append([input, int(column) + 1, row + 1])
        print(input, "is present", str(
            total_count), "times in the data set")

    else:
        print(column_name, "does not exist in dataset")

    # Prints matches if any were found
    if match:
        print()
        print("Details:")
        print("*********************************")
        print()

        for i in match:
            print(i[0], "is present in Column", i[1], "row", i[2])

# Deletes any column that contained a non-numerical value
def clean(boston_lists):
    temp = []

    # Non-numerical valued columns were replaced with ''
    # If '' is found, the column is not appended to temp
    for i in range(len(boston_lists)):
        if boston_lists[i][0] != '': 
            temp.append(boston_lists[i])

    # boston_lists will be set to equal temp
    return temp

###########################################################


def readCSV(file_2_name):
    # declares two empty lists of data
    listA = []
    listB = []
    # opens file to read with 'r'
    # 'with' allows opening and processing of file contents without
    # the need to call a close()
    # here we are assigning csv file to variable 'f'
    try:
        with open(file_2_name, 'r') as f:
        # COMMENT THIS IN FOR DEMO 
        # FILE DOESN'T EXIST
        #with open ('InputDataSample0.csv', 'r') as f:
        # CORRUPTED FILE 
        #with open ('Corrupted_InputDataSample.csv', 'r') as f:
        # UNEVEN ROWS AND COLUMNS 
        #with open ('Uneven_InputDataSample.csv', 'r') as f:
        
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
                    try:
                        listB.append(int(x[1]))
                    except ValueError:
                        print("\nNumber of columns do not match, please consider this with your results!")
        # returns lists
        return listA, listB
    except FileNotFoundError:
        print("\nINVALID FILE FOR STATISTICS SUMMARY CALCULATOR!")
        print("Please input a different file name before attempting to run the calculator.")
    except UnicodeDecodeError:
        print("\nCorrupted file, please provide one that works\n")


# calls function readCSV
dataSet = ""
try:
    file_1_name = sys.argv[1]
    file_2_name = sys.argv[2]
    dataSet = file_2_name
except IndexError:
    print("\nIncorrect number of command line arguments entered")
    print("Example: $ python3 calc.py Boston_Lyft_Uber_Data InputDataSample.csv")
    print("Program will exit\n")
    sys.exit(1)

readCSV(dataSet)
# 'dataSet' set equal to csv file


try:
    # returns length of data
    def count(dataSet):
        return len(dataSet)

    # returns unique values from data in string format
    def unique(dataSet):
        return len((set(dataSet)))

    # returns mean
    def mean(dataSet):
        try:
            return round(sum(dataSet) / len(dataSet))
            # COMMENT THIS IN FOR DEMO
            # DIVIDES BY ZERO
            #return round(sum(dataSet) / 0)
        except ZeroDivisionError:
            print("\nDivision by zero is taking place within mean calculation!")
            print("No mean values will be calculated or printed.")

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
        try:
            # mean of the data
            mean = sum(dataSet) / n
            # square deviations
            deviations = [(x - mean) ** 2 for x in dataSet]
            # variance
            variance = round(sum(deviations) / n)
        except ZeroDivisionError:
            print("\nDivision by zero taking place in variance calculation.")
            print("No variance or SD value will be calculated.")
        else:
            return variance
            # returns standard deviation
    def stddev(dataSet):
            try:
                return round(variance(dataSet)**0.5)
            except TypeError:
                print("\nDivision by zero in variance leads to TypeError in SD calculation.")


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
#except ZeroDivisionError:
    #print("\nCan not divide by zero, provide a different data set\n")

###########################################################
# Main for data processing
boston_lists = []
column_names = []
    
try:
    with open(sys.argv[1], 'r') as boston_data:
        data = []
        # if idx > 0 (because the first row on boston data is the column names)
        # and not 'NA' because NA is the input provided in the provided file for when the data is "empty"
        # may only apply to the "Boston_Lyft_Uber_Data.csv" that we were given and possibly needs to be changed
        #  if we are given a different data file
        for idx, line in enumerate(boston_data):
            # idx > 0 excludes the first row with column names
            # Also exclues rows with missing values
            if idx > 0 and 'NA' not in line:
                data.append(line)
            elif idx == 0:
                column_names.append(line)
        
        # Converts to dict to eliminate duplicates, then converts it back into a list
        data = list(dict.fromkeys(data))
        for idx, line in enumerate(data):
            # Skips row with column names
            words = line.split(',')

            # Makes boston_lists have # of lists by # of columns in csv file
            if idx == 0:
                for i in words:
                    boston_lists.append([])
            
            # Deletes all strings in words[] before appending to new list
            for j, value in enumerate(words):
                if not value.replace('.', '', 1).strip().isdigit():
                    words[j] = ''
            try:
                for i in range(len(boston_lists)):
                    boston_lists[i].append(words[i].strip())
            except IndexError:
                print("Uneven number of columns! Please consider using a different dataset!")
        boston_lists = clean(boston_lists)

        print("\nPlease give a command to search either a column by name")
        print("or the entire dataset.")
        print("\nExample: Search 3, Column1")
        print("Example: Search 2, DataSet")
        print("\nCommands in any other format will not be valid!")

        # INPUT VALIDATION!!
        # PREVENTS THE USER FROM GIVING INVALID INPUT!!
        while True:
            try:
                search_number, search_column = input("\nSearch ").split(", ")
                search_boston_lists(boston_lists, search_number, search_column)
                print('')
                break
            except:
                print("Oops! That was invalid input. Please try again.")

        boston_data.close()

    output_file = open('clean.txt', 'w')
    line = ""
    # Adds column names to output
    for names in column_names:        line += names + ","
    output_file.write(line + "\n")

     # Adds cleaned csv data to output
    line = ""
    for row in range(len(boston_lists[1])):
        for column in range(len(boston_lists)):
            #print(column)
            line += boston_lists[column][row] + ","
        line += "\n"
        output_file.write(line)
        
    

#if the following errors occur:
except FileNotFoundError:
    print("\nINVALID FILE FOR SEARCH FUNCTION!")
    print("Please input a different file name before attempting to run the search function.\n")
except UnicodeDecodeError:
    print("\nCorrupted file\n")
except TimeoutError:
    print("\nData processing took too long\n")
###########################################################
# Main for calculator
print("Statistics Summary Calculator:")
print("*********************************")
print()
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
try:
    listA, listB = readCSV(dataSet)
except TypeError:
    print("\nCan not calculate values related to invalid file!\n")

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
try:
    for i, dscrptr in enumerate(labels):
        # each row
        calc_row = [dscrptr]
        # special formatting case for indices 8 - 12
        if 12 >= i >= 8:
            # i starts at 8, subtract 8 to start at beginning
            # of percentile_values list with index 0
            #try:
                calc_row += [valueFunctions[i](listA, percentile_values[i-8])]
                calc_row += [valueFunctions[i](listB, percentile_values[i-8])]
            #except NameError:
                #print("\nFailure to load valid file leads to lists being undefined!")
            # formatting of all other indices
            # transferring values of 'listA', 'listB' to 'valueFunctions'
            # and then to 'calc_row' for display purposes
            # transferring values to 'valueFunctions' to iterate through
            # that list
        else:
            #try:
            calc_row += [valueFunctions[i](listA)]
            calc_row += [valueFunctions[i](listB)]
            #except NameError:
            #print("\nFailure to load valid file leads to lists being undefined!")

        # print all 'row's
        try:
            print(rowFormat.format(*calc_row))
        except TypeError:
            print("\nCalculation exception results in incomplete calculator output!")
        except IndexError:
            print("\nIndex error resulting from invalid input file!")
except NameError:
    print("\nFailure to load valid file leads to lists being undefined!")