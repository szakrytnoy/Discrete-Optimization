#!/usr/bin/python
# -*- coding: utf-8 -*-

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append([i, int(parts[0]), int(parts[1])])

    value = 0
    weight = 0
    taken = [0]*len(items)

    items_sorted = [[0 for x in range(3)] for y in range(item_count)]

    for i in range(item_count):
        for k in range(3):
            items_sorted[i][k] = items[i][k]

    max_ratio = items_sorted[0][1] / items_sorted[0][2]
    max_ratio_item = [0 for x in range(3)]
    max_ratio_item = items_sorted[0]
        
    for i in range(1, item_count):
        if items_sorted[i][1] / items_sorted[i][2] > max_ratio:

            max_ratio = items_sorted[i][1] / items_sorted[i][2]

            max_ratio_item = items_sorted[i]

            for j in range(i, 0, -1):
                items_sorted[j] = items_sorted[j - 1]
                
            items_sorted[0] = max_ratio_item

    for i in range(item_count):
        if capacity >= items_sorted[i][2]:
            taken[items_sorted[i][0] - 1] = 1
            value = value + items_sorted[i][1]
            capacity = capacity - items_sorted[i][2]
        else:
            break

##    for i in range(item_count):
##        if capacity >= items_sorted[i][2]:
##               
##            taken[items_sorted[i][0]] = 1
##            value = value + items_sorted[i][1]
##            capacity = capacity - items_sorted[i][2]
##        else:
##            break

    optimal = 0
        
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(optimal) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

