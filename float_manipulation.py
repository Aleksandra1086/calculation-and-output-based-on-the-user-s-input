'''● Create a new Python file in your folder called float_manipulation.py
● You will need to import the math module and use its built-in functions to
complete this task.
● Write a program that starts by asking the user to input 10 floats (these can
be a combination of whole numbers and decimals). Store these numbers
in a list.
● Find the total of all the numbers and print the result.
● Find the index of the maximum and print the result.
● Find the index of the minimum and print the result.
● Calculate the average of the numbers and round off to 2 decimal places.
Print the result.
● Find the median number and print the result.
'''

import math
import statistics

ten_nums_l = []
while True:
    num = float(input('Please input 10 decimal numbers: '))
    ten_nums_l.append(num)
    if len(ten_nums_l) == 10:
        break

print('Here is the list of the numbers you\'ve entered:')
print(ten_nums_l)

total = sum(ten_nums_l)

print('Total sum of the numberes you\'ve entered is: '+ str(total))

max_index = ten_nums_l.index(max(ten_nums_l))
print('The index number of the highest number in your list is: '+ str(max_index))

min_index = ten_nums_l.index(min(ten_nums_l))
print('The index number of the lowest number in your list is: '+ str(min_index))

print('The highest number you\'ve entered is: '+ str(max(ten_nums_l)))
print('The lowest number you\'ve entered is: '+ str(min(ten_nums_l)))

average = total/len(ten_nums_l)
median = statistics.median(ten_nums_l)

print(f'Average of numbers you\'ve entered is: {average}')

print('The average of your numbers rounded is: '+str(round(average)))

print('Median of the list of numbers you\'ve entered is: '+ str(median))
