'''
Write the code to do following:
   1. Generate list with lowercase and uppercase alphabet plus numbers
   2. Print 1st symbol of list
   3. Print last symbol
   4. Print 3rd from start and 3rd from the end
   5. Slice first 10 symbols
   6. Print only symbols with index, which divides on 2 without remaining
   7. Print only integer values from list
   8. Print only integer values from list * Reverse list using slice
   9. Convert base list into string
'''

import random

# 1. Generate list with lowercase and uppercase alphabet plus numbers
print("\n\t1. Generate list with lowercase and uppercase alphabet plus numbers\n")
s = ''
start = random.randint(5, 10)
end = start + random.randint(10, 15)
lis = (range(start, end))
for x in range(start, end):
    num = random.randint(1, 26)
    val = num if num < random.randint(1, 26) else chr(num + 64)
    s += str(val) if random.randint(1, 10) > 3 else str(val).lower()
print(s)

# 2. Print 1st symbol of list
print("\n\t2. Print 1st symbol of list\n")
print(s[0])

# 3. Print last symbol
print("\n\t3. Print last symbol\n")
print(s[-1])

# 4. Print 3rd from start and 3rd from the end
print("\n\t4. Print 3rd from start and 3rd from the end\n")
print("{}, {}".format(s[2], s[-3]))

# 5. Slice first 10 symbols
print("\n\t5. Slice first 10 symbols\n")
print(s[:10])

# 6. Print only symbols with index, which divides on 2 without remaining
print("\n\t6. Print only symbols with index, which divides on 2 without remaining\n")
res = ''
for i in range(len(s)):
    if i % 2 == 0:
        res += s[i] + " "
print(res)

# 7. Print only integer values from list
s = [5,'V',7,7,'J','Z',2,2,5,'P',4,3,1,4,1,'W','s']
print("\n\t7. Print only integer values from list\n")
l1 = []
for i in s:
    if type(i) == int:
        l1.append(i)
print(l1)

# 8. Reverse list using slice
print("\n\t8. Reverse list using slice\n")
print(s[::-1])

# 9. Convert base list into string
print("\n\t9. Convert base list into string\n")
s1 = str(s)
print (s1)
