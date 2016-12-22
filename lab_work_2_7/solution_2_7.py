'''
Write the code to do following:
  1. Write a script that creates a new output file called my file.txt
  2. Writes the string "Hello file world!" into it
  3. Write another code that opens myfile.txt in w+ mode
  4. Read and print its contents
  5. Write into "Hello file world 'Hello file' string new value 'my' 'Hello my file'"
  6. Save changes without file object close
'''

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