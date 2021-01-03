"""
Problem 3:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral
number between 1 and n (both included). Then the program should print the dictionary.
Suppose the following input is supplied to the program: 8, then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25,
6: 36, 7: 49, 8: 64}
Hints: In case of input data being supplied to the problem, it should be assumed to be a console input. Consider use
dict()
"""
# Solution:

integral_number = int(input())  # for the console input
dictionary = dict()  # declares a dictionary
for i in range(1, integral_number + 1):  # reads all numbers from 1 to the input
    dictionary[i] = i * i  # multiplies the number by itself and adds into the dictionary
print(dictionary)  # prints the dictionary
