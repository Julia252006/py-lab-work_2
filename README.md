Brain Academy. Python Course. Laboratory Work #2

Laboratory Work #2.1.

Write the code to do following:
    1. Create any variable with name var1
    2. Check type of var1 with type function
    3. Check is var1 is True
    4. Check is var1 is False
    5. Create var2 that equal to (var1 or True)
    6. Check is var2 is True
    7. Check is var2 is False
    8. Check result for var2 and var1

# 1. Create any variable with name var1
print("\n\t1. Create any variable with name var1\n")
var1 = 15
print("var1 = ", var1)

# 2. Check type of var1 with type function
print("\n\t2. Check type of var1 with type function\n")
print ("tape(var1) -> ", type(var1))

# 3. Check is var1 is True
print("\n\t3. Check is var1 is True\n")
print("bool(var1) -> ", bool(var1))

# 4. Check is var1 is False
print("\n\t4. Check is var1 is False\n")
print("bool(not var1) -> ", bool(not var1))

# 5. Create var2 that equal to (var1 or True)
print("\n\t5. Create var2 that equal to (var1 or True)\n")
var2 = var1
print("var2 = var = ", var1)

# 6. Check is var2 is True
print("\n\t7. Check is var2 is False \n")
print("bool(var2) -> ", bool(var2))

# 7. Check is var2 is False
print("\n\t7. Check is var2 is False\n")
print("bool(not var2) -> ", bool(not var2))

# 8. Check result for var2 and var1
print("\n\t8. Check result for var2 and var1\n")
print("bool(var2 == var1) -> ", bool(var2 == var1))


Brain Academy. Python Course. Laboratory Work #2

Laboratory Work #2.2.

Write the code to do following:
Generate sequence 5 integers long from range(0, 100)
Generate random float
Print variables above
Find max element from generated sequence
Make a floor division between max element and generated float
Find factorial of the result above
Shorten the code as much as possible
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
      
      
Brain Academy. Python Course. Laboratory Work #2

Laboratory Work #2.3.

Write the code to do following:
Generate string with lowercase and uppercase alphabet plus numbers
Print 1st symbol of string
Print last symbol
Print 3rd from start and 3rd from the end
Slice first 8 symbols
Print only symbols with index, which divides on 3 without remaining
Print the symbol of the middle of the string text
Reverse text using slice
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
print("\n\t1. Print 1st symbol of string\n")
print(s[0])

# 3. Print last symbol
print("\n\t1. Print last symbol\n")
print(s[-1])

# 4. Print 3rd from start and 3rd from the end
print("\n\t1. Print 3rd from start and 3rd from the end\n")
print("{}, {}".format(s[2], s[-3]))

# 5. Slice first 8 symbols
print("\n\t1. Slice first 8 symbols\n")
print(s[:8])

# 6. Print only symbols with index, which divides on 3 without remaining
print("\n\t1. Print only symbols with index, which divides on 3 without remaining\n")
res = ''
for i in range(len(s)):
    if i % 3 == 0:
        res += s[i] + " "
print(res)

# 7. Print the symbol of the middle of the string text
print("\n\t1. Print the symbol of the middle of the string text\n")
evLen = len(s) % 2 == 0
mid = len(s) // 2 + 1 if not evLen else len(s) // 2
print(s[mid] if not evLen else "{}, {}".format(s[mid - 1], s[mid]))

# 8. Reverse text using slice
print("\n\t1. Reverse text using slice\n")
print(s)
ch = ''
for i in range(0, len(s)):
    ch += s[len(s) - 1 - i]
print(ch)


Brain Academy. Python Course. Laboratory Work #2

Laboratory Work #2.4.

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


Brain Academy. Python Course. Laboratory Work #2

Laboratory Work #2.5

Write the code to do following:
   1. Create dict with 5 items, where keys will be country name and value - domain name, i.e. {Ukraine:UA}
   2. Create another dict with 5 items, where values of countries will be keys, and values will be the capitals i.e. {'UA': 'Kiev'}
   3. Add one more element to each dict above
   4. Print sentence "Domain for COUNTRY is DOMAIN." for each record in countries with the replace from dicts
   5. Print sentence "The capital of COUNTRY is CAPITAL" for each record in capitals with the replace from dicts
   6. Merge sentences above together with one cycle
   7. Add to each value of first dict another two domains: COM and GOV
   
   
 Brain Academy. Python Course. Laboratory Work #2
   
Laboratory Work #2.6

Write the code to do following:
  1. Generate two sets with not unique numbers and few symbols
  2. Print 1st set
  3. Create tuple from intersection of first and second set
  4. Create tuple from difference first and second set
  5. Slice first 3 symbols from first tuple
  6. Print only symbols with numbers from second set
  7. Reverse tuple using slice
  8. Convert both tuples into list
  
  # 1. Generate two sets with not unique numbers and few symbols
print("\n\t1. Generate two sets with not unique numbers and few symbols\n")
s1 = {1, 2, 3, 'A'}
s2 = {4, 5, 3, 'A'}
print(s1, s2)

# 2. Print 1st set
print("\n\t2. Print 1st set\n")
print(s1)

# 3. Create tuple from intersection of first and second set
print("\n\t3. Create tuple from intersection of first and second set\n")
t1 = tuple(s1 & s2)
print(t1)

# 4. Create tuple from difference first and second set
print("\n\t4. Create tuple from difference first and second set\n")
t2 = tuple(s1 - s2)
print(t2)

# 5. Slice first 3 symbols from first tuple
print("\n\t5. Slice first 3 symbols from first tuple\n")
l1 = list(s1)
print(l1[:3])

# 6. Print only symbols with numbers from second set
print("\n\t6. Print only symbols with numbers from second set\n")
l2 = list(s2)
l3 = []
for i in l2:
    if type(i) == int:
        i = l3.append(i)
print(l2)

# 7. Reverse tuple using slice
print("\n\t7. Reverse tuple using slice\n")
l4 = list(t2)
list.reverse(l4)
print(l4)

# 8. Convert both tuples into list
print("\n\t8. Convert both tuples into list\n")
l5 = list(t1 + t2)
print(l5)


Brain Academy. Python Course. Laboratory Work #2

Laboratory Work #2.7

Write the code to do following:
  1. Write a script that creates a new output file called my file.txt
  2. Writes the string "Hello file world!" into it
  3. Write another code that opens myfile.txt in w+ mode
  4. Read and print its contents
  5. Write into "Hello file world 'Hello file' string new value 'my' 'Hello my file'"
  6. Save changes without file object close
  
  # 1. Write a script that creates a new output file called my file.txt
print("\n\t1. Write a script that creates a new output file called my file.txt\n")
f = open('my_file.txt', 'w')

# 2. Writes the string "Hello file world!" into it
print("\n\t2. Writes the string 'Hello file world!' into it\n")
f.write('Hello file world!')

# 3. Write another code that opens my file.txt in r+ mode
print("\n\t3. Write another code that opens my_file.txt in r+ mode\n")
f = open('my_file.txt', 'r+')

# 4. Read and print its contents
print("\n\t4. Read and print its contents\n")
print(f.read())

# 5. Write into "Hello file world 'Hello file' string new value 'my' 'Hello my file'"
print("\n\t5. Write into 'Hello file' string new value 'my' 'Hello my file'\n")
f = open('my_file.txt', 'r+')
f.seek(len('Hello '))
f.write('my file world!')

# 6. Save changes without file object close
print("\n\t6. Save changes without file object close\n")
f.close()