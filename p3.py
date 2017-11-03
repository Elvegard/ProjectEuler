import numpy as np
import sys

findInNumber = 600851475143
stop = root = int(np.sqrt(findInNumber))
print("root: ", root)

# mark all numbers as true
p = np.ones((1, stop+1), dtype=bool)



def printPrimes(p):
    """
    Loops through array and finds all marked as True (primes).
    Return an array with only prime numbers.
    """
    prime_array = np.array([])
    idx = 2
    numb_primes = 0;
    while (idx**2 <= findInNumber):
        if p[0][idx] == True:
            numb_primes += 1
            prime_array = np.append(prime_array, idx)
        idx += 1
    print("Total primes: ", numb_primes)
    return prime_array
        

def markNonPrimes(numb, p):
    """
    Mark all non primes in array with false
    """
    n = numb + numb
    while (n**2 <= findInNumber):
        if p[n] == True:
            p[n] = False
        n += numb
    return p


def findPrimesInNumber(numb, prime_array):
    """
    Find all the primes in given number
    """
    primes_in_number = np.array([])

    if numb in prime_array:
        primes_in_number = np.append(primes_in_number, numb)
    else:
        n = numb
        for prime in prime_array:
            if prime**2 > findInNumber:
                break
            while (numb % prime) == 0:
                numb = numb/prime
                primes_in_number = np.append(primes_in_number, prime)
                
    return primes_in_number
        

# mark numbers that are not primes as false
for i in range(2, stop):
    p[0] = markNonPrimes(i, p[0])

# retrive array with primes only
prime_array = printPrimes(p)

# find primes in current number
primes_in_array = findPrimesInNumber(findInNumber, prime_array)
print("Primes in ", findInNumber, ": ", primes_in_array)


    
