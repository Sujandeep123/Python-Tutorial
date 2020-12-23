#%% ==========  ========== %%#

from os import error


prices = {
  'apple' : 2,
  'banana' : 4
}

# find apple's price
prices['apple']

prices['banana']

prices['apple'] = 3

prices['apple']


my_fruit = 'dragon fruit'

prices[my_fruit]
# user's fruit doesn't exist, so it shows error. But i want the program to handle the error, so i will use `get` method

prices.get(my_fruit)
# now it doesn't shows any error, yay :), thats good. But the user has no idea what happend

msg = prices.get(my_fruit, f'Bad day dude, {my_fruit} is not available' )

my_prices = prices.get(my_fruit, [] )



# Conclusion

# What is the use of dict.get function ?
# 1. It supresses error
# 2. It returns placeholer value