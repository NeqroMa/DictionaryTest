"""
Sample dictionary init from CSV
in the simple case of the CSV being
exactly key-value pairs

"""
import os
import csv

my_dir = os.path.dirname(os.path.realpath(__file__))
filename = 'dictionary_test.csv'

my_dict = {}

with open(my_dir + '/' + filename, 'r') as f:
    read_file = csv.reader(f)

    for row in read_file:
        key = int(row[0])
        value = row[1]
        my_dict[key] = value.lstrip()

print(my_dict)


print(my_dict[1])
