import numpy as np
import sys

print("                   // ProjectEuler problem 7 \\")
print()
print("What is the 10 001st prime number?")
print("---------------------------------------------------------------------------")
print()

find_number_of_primes = 10001
stop = 10**10
      
number_of_primes_found = 1
primes = np.array([2])


for i in range(3, stop):
    is_prime = True
    for j in primes:
        if (i%j == 0):
            is_prime = False
    if is_prime:
        primes = np.append(primes, i)
        number_of_primes_found += 1

    if number_of_primes_found >= find_number_of_primes:
        print("Number of primes found: ", number_of_primes_found)
        print("Highest prime: ", primes[len(primes)-1])
        sys.exit(0)
            

            


