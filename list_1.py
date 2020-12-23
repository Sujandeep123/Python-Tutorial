## Python Data-Structure Series

# Data Types:
  # - numeric : int, float
  # - string
  # - boolean : [True, False]

# Basic Data Structures
  # 1. List: [v, ]
  # 2. Tuple: (v, )
  # 3. Set: {v, }
  # 4. Dictionary: {k : v}

#%% ========== List (Array) ========== %%#

# list definitions

# - numerically indexed collection of values

# - array is composed of
#   - keys(indexes) which are implict(doesn't need to be defined by user)
#   - values

empty_list = []

# list constructor, refer object constructor (classe)
emply_list = list()

list_of_random_data = [12, 'Sujan', True, '12', 12.0]

# length of array
len(list_of_random_data)

## read write list ##

# read single element
print(list_of_random_data[0])
print(list_of_random_data[-1])

# read range of elements
# array[<start>:<end>:<step_size>]
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print(array[0:10])
print(array[-13:-1])
# stepping
print(array[0:20:5])


# writing to array

# writing at single point
list_of_random_data[3] = 'something new'
list_of_random_data

# writing in a range
list_of_random_data[0:2] = ['new first', 'new second']
list_of_random_data

# appending single element to an array
list_of_random_data.append('new')
list_of_random_data

# append multiple element to an array
new_array = ['pratuat', 'rome', '40']
list_of_random_data.extend(new_array)
list_of_random_data

# deleting single or range of element by index in an array
del(list_of_random_data[3])
del(list_of_random_data[0:3])
list_of_random_data

## Other functions for list

# 'append',
# 'extend',
#>> 'clear',
#>> 'copy',
#>> 'index',
#>> 'insert',

# 'count',
arr = ['sujan', 'some name', 12, 'sujan']
arr.count(12)

# 'remove',
arr = ['sujan', 'some name', 12, 'sujan']
arr.remove('sujan')


####### [Review] the difference between del(array[i]) and array.remove(value) #######

# 'pop': remove object by index and return the object
arr = ['sujan', 'some name', 12, 'sujan']
y = arr.pop(1)
print(arr)

# 'reverse',
arr = ['sujan', 'some name', 12, 'sujan']
arr.reverse()
print(arr)

# 'sort'
arr = ['banana', 'aplple', 'box']
arr.sort(reverse=False)
print(arr)

# Next Time

# for loops in list
# inclusins in list
# numeric len, sum, min, max






#%% ========== Dictionary ========== %%#
