# TUPLES AND SETS

### Tuples ###

# lists are MUTABLE objects, they can be modified

my_list = ['kathmandu', 'lalitpur', 'bhaktapur']

my_list.remove('lalitpur')
my_list.append('bharatpur')
my_list.pop()


# tuple are IMMUTABLE objects, they cannot be modified
my_list = ['kathmandu', 'lalitpur', 'bhaktapur']
my_tuple = ('kathmandu', 'lalitpur', 'bhaktapur')


## access function that applies to list also applies to tuple

len(my_list)
len(my_tuple)


# list slicing
my_list[1]
my_tuple[1]
my_list[0:2]
my_tuple[0:2]


# for loops
for item in my_list:
  print(item)

for item in my_tuple:
  print(item)


# convert array to tuple and vice-versa

list(my_tuple)

tuple(my_list)


## Takeaway excercise

items = "olive cheese steak cornflakes pasta corn beans eggs milk".split()
prices = [1.99, 1.69, 4.5, 2.5, .55, 1.69, 1.4, 1.29, .79]

discounted_items = "steak eggs milk"
basket_items = "olive cheese pasta corn eggs"

# Item price are specified in 'items' and 'prices' array
# Items in 'discounted_items' have discounts of 50%
# Find the the total price of 'basket_items'
