'''
Write the code to perform following task:
        1. Generate sequence 5 integers long from range(0, 100)
        2. Generate random float
        3. Print variables above
        4. Find max element from generated sequence
        5. Make a floor division between max element and generated float
        6. Find factorial of the result above
        7. Shorten the code as much as possible
'''

import random
import math

# 1. Generate sequence 5 integers long from range(0, 100)
print("\n\t1. Generate sequence 5 integers long from range(0, 100)\n")
rList = random.sample(range(100), 5)
print ("List = random.sample(range(100), 5)")

# 2. Generate random float
print("\n\t1. Generate random float\n")
fRand = random.random()
print ("fRand = random.random() = {}". format(fRand))

# 3. Print variables above
print("\n\t1. Print variables above\n")
print("rList = {}. fRand = {}".format(rList, fRand))

# 4. Find max element from generated sequence
print("\n\t1. Find max element from generated sequence\n")
max_in_list = max(rList)
print("max_in_list = max(rList) = {}".format(max_in_list))

# 5. Make a floor division between max element and generated float
print("\n\t1. Make a floor division between max element and generated float\n")
print("max_in_list // fRand = {}".format(max_in_list // fRand))

# 6. Find factorial of the result above
print("\n\t1. Find factorial of the result above\n")
print("math.factorial(max_in_list // fRand) = {}"
      .format(math.factorial(max_in_list // fRand)))