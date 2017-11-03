import numpy as np
import sys

print("                   // ProjectEuler problem 4 \\")
print()
print("Find the largest palindrome made from the product of two 3-digit numbers.")
print("-------------------------------------------------------------------------")
print()

max_number = 999*999
min_number = 100*100
print("Maximum possible number: ", max_number)
print("Minimum possible number: ", min_number)


def checkPalindrome(i, j):
    numb = i * j;
    number = str(numb)
    first_part = number[0:int(len(number)/2)]
    second_part = number[int(len(number)/2):]
    first_part_reverse = first_part[::-1]

    if first_part_reverse == second_part:
        return True
    else:
        return False

max_found = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if checkPalindrome(i, j):
            if (i*j) > max_found:
                max_found = (i*j)

print("Max: ", max_found)
