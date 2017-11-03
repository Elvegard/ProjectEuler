import numpy as np
import sys

print("                   // ProjectEuler problem 6 \\")
print()
print("Find the difference between the sum of the squares of the first one hundred")
print("natural numbers and the square of the sum.")
print("---------------------------------------------------------------------------")
print()


from_value = 1
to_value = 101

def squareOfSum(from_value, to_value):
    return_value = 0
    for i in range(from_value, to_value):
        return_value += i
    return return_value**2


def squareOfNumbers(from_value, to_value):
    return_value = 0;
    for i in range(from_value, to_value):
        return_value += i**2
    return return_value


square_of_sum = squareOfSum(from_value, to_value)
square_of_numbers = squareOfNumbers(from_value, to_value)

print("Square of sum: ", square_of_sum)
print("Square of numbers: ", square_of_numbers)
print("Difference: ", abs(square_of_numbers - square_of_sum))
