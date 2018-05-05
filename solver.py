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
        
    ##    print('capacity', capacity)
    my_table = [[0 for x in range(item_count + 1)] for y in range(capacity + 1)]

    ##    for i in range(item_count):
    ##        print(items[i])
    ##        print()

    for i in range(1, item_count + 1):
        for c in range(capacity + 1):
            if c < items[i - 1][2]:
                my_table[c][i] = my_table[c][i - 1]
            else:
                if my_table[c][i - 1] < items[i - 1][1] + my_table[c - items[i - 1][2]][i - 1]:
                    my_table[c][i] = items[i - 1][1] + my_table[c - items[i - 1][2]][i - 1] 
                else:
                    my_table[c][i] = my_table[c][i - 1]
                        
    value = my_table[capacity][item_count]

    for i in range(item_count, 0, -1):
        if my_table[c][i] != my_table[c][i - 1]:
            taken[i - 1] = 1
            c = c - items[i - 1][2]
                    
    ##    for c in range(capacity + 1):
    ##        print(my_table[c])
    ##        print()

    optimal = 1
        
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

