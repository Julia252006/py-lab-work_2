'''
Write the code to do following:
  1. Generate two sets with not unique numbers and few symbols
  2. Print 1st set
  3. Create tuple from intersection of first and second set
  4. Create tuple from difference first and second set
  5. Slice first 3 symbols from first tuple
  6. Print only symbols with numbers from second set
  7. Reverse tuple using slice
  8. Convert both tuples into list
'''

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
