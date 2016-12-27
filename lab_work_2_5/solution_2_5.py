'''
Write the code to do following:
   1. Create dict with 5 items, where keys will be country name and value - domain name, i.e. {Ukraine:UA}
   2. Create another dict with 5 items, where values of countries will be keys, and values will be the capitals i.e. {'UA': 'Kiev'}
   3. Add one more element to each dict above
   4. Print sentence "Domain for COUNTRY is DOMAIN." for each record in countries with the replace from dicts
   5. Print sentence "The capital of COUNTRY is CAPITAL" for each record in capitals with the replace from dicts
   6. Merge sentences above together with one cycle
   7. Add to each value of first dict another two domains: COM and GOV
'''

# 1. Create dict with 5 items, where keys will be country name and
# value - domain name, i.e. {Ukraine:UA}
print("\n\t1. Create dict with 5 items, where keys will be) "
      " + (country name and value - domain name, i.e. {Ukraine:UA}\n")
dic = {'Ukraine': 'UA',
       'Poland': 'PL',
       'Austria': 'AT',
       'Cyprus': 'CY',
       'Germany': 'DE'}
print(dic)

# 2. Create another dict with 5 items, where values of
# countries will be keys, and values will be the capitals i.e. {'UA': 'Kiev'}
print("\n\t2. Create another dict with 5 items, where values) + "
      "(of countries will be keys, and values will be the capitals i.e. {'UA': 'Kiev'}\n")
dic1 = {'UA': 'Kiev',
        'PL':'Warsaw',
        'AT':'Vein',
        'CY': 'Nicosia',
        'DE':'Berlin'}
print(dic1)

# 3. Add one more element to each dict above
print("\n\t3. Add one more element to each dict above\n")
dic.update({'Spain': 'SP'})
dic1.update({'SP': 'Madrid'})
print(dic)
print(dic1)

# 4. Print sentence "Domain for COUNTRY is DOMAIN." for each record
# in country with the replace from dicts
print("\n\t4. Print sentence \"Domain for COUNTRY is DOMAIN.\" for) + "
      "(each record in countries with the replace from dicts\n")
for key, value in dic.items():
      print("Domain for {} is {}.".format(key, value))


# 5. Print sentence "The capital of COUNTRY is CAPITAL" for each record
# in capitals with the replace from dicts
print("\n\t5. Print sentence \"The capital of COUNTRY is CAPITAL\"" +
      " for each record in capitals with the replace from dicts\n")
for key, value in dic.items():
    print("The capital of {} is {}".format(key, value))


# 6. Merge sentences above together with one cycle
print("\n\t6. Merge sentences above together with one cycle\n")
for key, value in dic.items():
    print("Domain for {} is {}.The capital is {}".format(key, value, dic1[value]))


# 7. Add to each value of first dict another two domains: COM and GOV
print("\n\t7. Add to each value of first dict another two domains: COM and GOV\n")
for key, value in dic.items():
    dic[key] = [value, 'COM', 'GOV']
print(dic)