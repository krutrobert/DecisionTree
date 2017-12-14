from decision_tree import build_tree
from decision_tree import print_tree
from decision_tree import print_leaf
from decision_tree import classify
from decision_tree import get_header
from decision_tree import set_header
from decision_tree import get_unique_values
import csv

training_data = []

with open('data.csv', encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        new_row = []
        for item in row[0].split(','):
            new_row.append(item)
        training_data.append(new_row)

my_tree = build_tree(training_data)

print_tree(my_tree)
print()

testing_data = []

for i in range(len(get_header())-1):
    ask = 'Введіть ' + str(get_header()[i]) + str(get_unique_values(training_data, i)) + ': '
    user_input = input(ask)
    testing_data.append(user_input)

print("Передбачено: %s" % (print_leaf(classify(testing_data, my_tree))))

input()