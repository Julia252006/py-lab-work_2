'''
Write the code to do following:
    1. Generate string with lowercase and uppercase alphabet plus numbers
    2. Print 1st symbol of string
    3. Print last symbol
    4. Print 3rd from start and 3rd from the end
    5. Slice first 8 symbols
    6. Print only symbols with index, which divides on 3 without remaining
    7. Print the symbol of the middle of the string text
    8. Reverse text using slice
'''

import random

# 1. Generate string with lowercase and uppercase alphabet plus numbers
print("\n\t1. Generate string with lowercase and uppercase alphabet plus numbers\n")
s = ''
start = random.randint(5, 10)
end = start + random.randint(10, 15)
for x in range(start, end):
    num = random.randint(1, 26)
    val = num if num < random.randint(1, 26) else chr(num + 64)
    s += str(val) if random.randint(1, 10) > 3 else str(val).lower()
print(s)

# 2. Print 1st symbol of string
print("\n\t2. Print 1st symbol of string\n")
print(s[0])

# 3. Print last symbol
print("\n\t3. Print last symbol\n")
print(s[-1])

# 4. Print 3rd from start and 3rd from the end
print("\n\t4. Print 3rd from start and 3rd from the end\n")
print("{}, {}".format(s[2], s[-3]))

# 5. Slice first 8 symbols
print("\n\t5. Slice first 8 symbols\n")
print(s[:8])

# 6. Print only symbols with index, which divides on 3 without remaining
print("\n\t6. Print only symbols with index, which divides on 3 without remaining\n")
res = ''
for i in range(len(s)):
    if i % 3 == 0:
        res += s[i] + " "
print(res)

# 7. Print the symbol of the middle of the string text
print("\n\t7. Print the symbol of the middle of the string text\n")
evLen = len(s) % 2 == 0
mid = len(s) // 2 + 1 if not evLen else len(s) // 2
print(s[mid] if not evLen else "{}, {}".format(s[mid - 1], s[mid]))

# 8. Reverse text using slice
print("\n\t8. Reverse text using slice\n")
print(s)
ch = ''
for i in range(0, len(s)):
    ch += s[len(s) - 1 - i]
print(ch)