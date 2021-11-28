# NAME: Salvador Vargas, Samuel Kaing, Wesley Tam
# ASGT: Class Project
# ORGN: CSUB - CMPS 3500
# FILE: calc.py
# DATE: 11/13/2021

# PYTHON IMPLEMENTATION OF A CUSTOM STATISTICS SUMMARY CALCULATOR

def readCSV():
    # declares two empty lists of data
    listA = []
    listB = []
    # opens file to read with 'r'
    # 'with' allows opening and processing of file contents without
    # the need to call a close()
    # here we are assigning csv file to variable 'f'
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

# calls function readCSV
readCSV()

# 'dataSet' set equal to csv file
dataSet = 'InputDataSample.csv'

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
    frequency={}
    # looping through list recording frequency
    # of each value
    for number in dataSet:
        frequency.setdefault(number,0)
        frequency[number]+=1
    # converting values into list using
    # python built-in '.values()' function
    # we have multiple values that appear an
    # equal number of times, therefore we have several modes
    # now creating a list of those values
    highestFrequency=max(frequency.values())
    highestFreqLst=[]
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

# declares top row
topRow = ['Descriptor', 'Column A', 'Column B']
# inserts "*" between rows
spacer = ['**********', '********', '********']
# declares labels
labels = ['Count', "Unique", 'Mean', 'Median', 'Mode','SD', 
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
    row = [dscrptr]
    # special formatting case for indices 8 - 12
    if 12 >= i >= 8:
        # i starts at 8, subtract 8 to start at beginning
        # of percentile_values list with index 0
        row += [valueFunctions[i](listA, percentile_values[i-8])]
        row += [valueFunctions[i](listB, percentile_values[i-8])]
        # formatting of all other indices
        # transferring values of 'listA', 'listB' to 'valueFunctions'
        # and then to 'row' for display purposes
        # transferring values to 'valueFunctions' to iterate through
        # that list
    else:
        row += [valueFunctions[i](listA)]
        row += [valueFunctions[i](listB)]
    # print all 'row's
    print(rowFormat.format(*row))
