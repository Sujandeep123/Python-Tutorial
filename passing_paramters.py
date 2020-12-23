#%% ========== Pass by value vs reference ========== %%#

# Topics to revise

# Pass by values: Basic datatypes (boolean, int, float, string)
# Pass by references: Other datatypes (list, array or any other objects)

def func_a(input_list):
  input_list += input_list

  return input_list

string_meow = 'meow' # string is basic data type
list_meow = ['m', 'e', 'o', 'w'] # array is non-basic data type

# Are the value printed by 1st and 2nd line are same ? why or why not ?
print('Inside function: ', func_a(string_meow))
print('Outside function: ', string_meow)

# Are the value printed by 1st and 2nd line are same ? why or why not ?
# print('Inside function: ', func_a(list_meow))
# print('Outside function: ', list_meow)

#%% ==========  ========== %%#

# old_value = 10
old_value = [10]

def func_a(value):
  value += value
  print(value)


func_a(old_value)

print(old_value)

#%% ==========  ========== %%#

person = ['sujan', 'shrestha']

def afunc (person):
  person.append('chaakupaat')
  print(person)


afunc(person.copy())
print(person)

afunc(person)
print(person)
