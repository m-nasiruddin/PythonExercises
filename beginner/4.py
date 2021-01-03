"""
Problem 4:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which
contains every number.
Suppose the following input is supplied to the program: 34, 67, 55, 33, 12, 98, then the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
Hints: In case of input data being supplied to the question, it shoulb be assumed to be a console input. tuple() method
can convert list to tuple.
"""
# Solution:

values = input()  # accepts a sequence of comma-separated numbers from console
a_list = values.split(',')  # generates a list
a_tuple = tuple(a_list)  # generates a tuple
print(a_list)  # prints the list
print(a_tuple) # prints the tuple
