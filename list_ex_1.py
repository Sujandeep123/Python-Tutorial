
### Excercise 1 ###

fruits = "apple banana cherry pear tomato pineapple mango".split()
vegetables = "potato spinach onions beans".split()
basket = 'apple pear salame ice-cream onions mango'.split()

# "basket" is a collection of items bought by a shopper. For each item in basket, print type of item if it is fruit or vegetable as listed in first two arrays

# Example:
# if basket = ['mango', 'onions', 'ketcup']

# Output:
# mango is a fruits
# oinion is a vegetables
# ketcup neither a fruit nor a vegetable


### Excercise 2 ###

# Building upon Excercise 1, create a new list of fruit items in the basket.

### Excercise 3 ###

# Below are the items in a fruit shop and their prices.

fruits = "apple banana cherry pear tomato pineapple mango".split()
fruit_prices = [120, 0, 400, 200, 0, 110, 80]

# This is the list of items in a user's basket. Compute the total price for the user.
basket = ['pear', 'cherry', 'mango']

### Excercise 4 ###
fruit_prices = [120, 0, 400, 200, 0, 110, 80]

# Given is an array of fruit prices for 7 fruits. Due to mistake, a computer operator entered 0 instead of 100 in the price list.append
# Now correct the mistake by replacing all 0 prices by 100

#%%
### Excercise 5 ###

fruits = "apple banana cherry pear tomato pineapple mango".split()
fruit_prices = [120, 100, 400, 200, 100, 110, 80]
basket = 'apple pear salame ice-cream onions mango'.split()

# Given fruit prices, print the total sum of prices for fruits in the basket.

sum_of_fruit_prices = 0

for item in basket:
  print(item, sum_of_fruit_prices, fruits)
  if item in fruits:
    index_of_fruit = fruits.index(item)
    price_of_fruit = fruit_prices[index_of_fruit]

    sum_of_fruit_prices = sum_of_fruit_prices + price_of_fruit

print(sum_of_fruit_prices)
#%%
