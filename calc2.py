def read_csv():
    column_a = []
    column_b = []
    with open('InputDataSample2.csv', 'r') as f:
        for ix, line in enumerate(f):
            if ix > 0:
                words = line.split(',')
                column_a.append(int(words[0]))
                column_b.append(int(words[1].strip()))
    return column_a, column_b

read_csv()

def count(data):
    # returns length of data
    return len(data)

def unique(data): 
    # returns unique values from data in string format
    return len(str(list((set(data)))))

def mean(data):
    # returns mean
    return sum(data) / len(data)

def median(data):
    # returns median
    length = len(data)
    if length%2 == 0:
        # for even length data 
        return str([data[length%2], data[(length%2) + 1]])
    else:
        # median for odd length data
        return data[length%2]

def mode(data):
    # returns mode 
    return max(set(data), key = data.count)

def variance(data):
    # returns variance
    length = len(data)
    ss = sum((x-mean(data))**2 for x in data) 
    pvar = ss/length

    return pvar

def stddev(data):
    # returns standard deviation
    return variance(data)**0.5

def minimum(data):
    # returns minimum value from data
    return min(data)

def maximum(data):
    # returns maximum value from data
    return max(data)

def percentile(data, percentile):
    # returns percentile th value from data
    length = len(data)
    p = length * percentile / 100
    if p.is_integer():
        return sorted(data)[int(p)]
    else:
        if p > int(p):
            p += 1
        return sorted(data)[int(p) - 1]

header = ['Descriptor', 'Column A', 'Column B']
descriptors = ['Count', "Unique", 'Mean', 'Median', 'Mode','Standard Deviation', 
                'Variance', 'Minimum', '20 Percentile (P20)', '40 Percentile (P40)', 
                '50 Percentile (P50)', '60 Percentile (P60)', '80 Percentile (P80)', 
                'Maximum']
descriptor_functions = [count, unique, mean, median, mode, stddev, 
                        variance, minimum, percentile, percentile, 
                        percentile, percentile, percentile, maximum]

percentile_values = [20, 40, 50, 60, 80]

column_a, column_b = read_csv()

# returns data in format
row_format = "{:>20}" * 3
print(row_format.format(*header))
for ix, descriptor in enumerate(descriptors):
    row = [descriptor]
    if 13 > ix >= 8:
        row += [descriptor_functions[ix](column_a, percentile_values[ix-8])]
        row += [descriptor_functions[ix](column_b, percentile_values[ix-8])]
    else:
        row += [descriptor_functions[ix](column_a)]
        row += [descriptor_functions[ix](column_b)]
    print(row_format.format(*row))
