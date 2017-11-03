import numpy as np
import sys

print("                   // ProjectEuler problem 5 \\")
print()
print("What is the smallest positive number that is evenly divisible by all of")
print("the numbers from 1 to 20?")
print("-------------------------------------------------------------------------")
print()

max = 10**9
start = 2520


def checkDivisible(number):
    for k in range(2, 20):
        if not(number%k == 0):
            return False
    return True

for i in range(start, max):
    if checkDivisible(i):
        print("Minimum: ", i)
        sys.exit(0)
