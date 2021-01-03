"""
Problem 1:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000
and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints: Consider using range(#begin, #end) method.
"""
# Solution:

numbers = []  # declares a list
for i in range(2000, 3201):  # reads all numbers from 2000 to 3201
    if (i % 7 == 0) and (i % 5 != 0):  # finds a number which is divisible by 7 but not multiple of 5
        numbers.append(str(i))  # appends the number in the list
print(','.join(numbers))  # prints in a comma-separated sequence on a single line
