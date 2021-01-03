"""
Problem 2:
Write a program which can compute the factorial of a given number.
Suppose the following input is supplied to the program: 8, then the output should be: 40320
"""
# Solution:


def factorial(num):  # this is a recursive function
    if num == 1:
        return 1
    return number * factorial(num - 1)  # calls the same function


number = int(input())  # take the number as an input
print(factorial(number))  # call the recursive function
