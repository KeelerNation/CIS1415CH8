my_dict = {'John': '55', 'Brian': '50', "Bob": '84', 'Bill': '92'}

# prints the keys and values best used in a loop, there are also methods for just values and keys
for key, values in my_dict.items():
    print('Name: %s, Age: %s' % (key, values))
print('')

#gets rid of a key value form the dictionary
my_dict.pop('Bill')
print(my_dict)
print('')

#adds onto the dictionary
my_dict.update({'John Jr': '34'})
print(my_dict)
print('')

#turns the dictionary into a list
value = list(my_dict.values())
key = list(my_dict.keys())
print(my_dict.values())
print(my_dict.keys())
print('')

#turns two lists into dictionarys
dict(zip(key, value))
print(my_dict)