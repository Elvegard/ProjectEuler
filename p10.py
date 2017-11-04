import numpy as np
import sys

print("                   // ProjectEuler problem 10 \\")
print()
print("Find the sum of all the primes below two million.")
print("---------------------------------------------------------------------------")
print()


def checkIfPrime(number, array):
    """
    Check if index is True, i.e. number is a prime number.
    A False indicate that the number is not a prime number.
    """
    if array[0][number]:
        return True
    else:
        return False
    

    
def setAsNotPrime(number, array):
    """
    Marks number in array as False, i.e. not a prime number.
    """
    array[0][number] = False
    return array



def markCompositeNumber(prime, array):
    """
    Mark composite numbers in array as False, i.e. not a prime number.
    """
    markNumber = prime + prime
    while markNumber < len(array[0]):
        array = setAsNotPrime(markNumber, array)
        markNumber += prime

    return array


def getPrimeNumberArray(array):
    """
    Return an array with only the prime numbers
    """
    primes = np.array([])
    for number in range(1, len(array[0])-1):
        if array[0][number]:
            primes = np.append(primes, number)
    return primes

    
    
def getPrimes(stop_number):
    # Set all numbers as potentially prime number, including 0
    primes = np.full((1, stop_number+1), True, dtype=bool)

    # Mark 0 and 1 as not prime
    primes = setAsNotPrime(0, primes)
    primes = setAsNotPrime(1, primes)

    # Check if number is prime and mark composite numbers
    for number in range(2, len(primes[0]-1)):
        if checkIfPrime(number, primes):
            primes = markCompositeNumber(number, primes)

    return getPrimeNumberArray(primes)


def sumNumbers(array):
    sum = 0
    for number in range(0, len(array)):
        sum += array[number]
    return sum

primes = getPrimes(2000000)

sum = sumNumbers(primes)
print("Sum of primes: ", sum)
