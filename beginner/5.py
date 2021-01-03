"""
Problem 5:
Define a class which has at least two methods: getString, to get a string from console input and printString, to print
the string in upper case. Also please include simple test function to test the class methods.
Hints: Use __init__ method to construct some parameters.
"""
# Solution:


class GetPrintString(object):
    def __init__(self):
        self.string = ''

    def get_string(self):
        self.string = input()

    def print_string(self):
        print(self.string.upper())


stringObject = GetPrintString()
stringObject.get_string()
stringObject.print_string()
