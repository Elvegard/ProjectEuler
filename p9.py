import numpy as np
import sys

print("                   // ProjectEuler problem 9 \\")
print()
print("There exists exactly one Pythagorean triplet for which a + b + c = 1000.")
print("Find the product abc.")
print("---------------------------------------------------------------------------")
print()

max = 1000

for a in range(1, max):
    for b in range(1, max):
        for c in range(1, max):
            if not(a==b) and not(a==c) and not(b==c):
                if (a+b+c) == 1000:
                    if (a**2 + b**2) == c**2:
                        print(a, "^2 + ", b, "^2 = ", c, "^2")
                        print(a**2, " + ", b**2, " = ", c**2)
                        print("Product a*b*c: ", a, "x", b, "x", c, "= ", (a*b*c))
                        sys.exit(0)
