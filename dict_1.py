#%% ========== Nested Dictionaries ========== %%#


fruits = {
  'apple': 2,
  'organe' : 4
}

veggies = {
  'onion' : 4,
  'potato' : 3
}

item_prices = {
  'fruit_price' : fruits,
  'vegetable_prices' : veggies,
  'customers' : ['jim', 'tim']
}


#%% ========== Iterating dictionary elements in for loop ========== %%#

price_list = {
  'olive': 1.99,
  'cheese': 1.69,
  'steak': 4.5,
  'cornflakes': 2.5,
  'pasta': 0.55,
  'corn': 1.69,
  'beans': 1.4,
  'eggs': 1.29,
  'milk': 0.79
}

for key, value in price_list.items():
  print(key, value)

#%% ========== Accessing and changing values ========== %%#

# Access values using keys
price_list['corn']

# Modify values by keys
price_list['corn'] = 10

# 'get' acessor for default value
price_list.get('olive', 5)

#%% ========== Excercies ========== %%#

price_list = {
  'olive': 1.99,
  'cheese': 1.69,
  'steak': 4.5,
  'cornflakes': 2.5,
  'pasta': 0.55,
  'corn': 1.69,
  'beans': 1.4,
  'eggs': 1.29,
  'milk': 0.79
}

# for items not present in dictionary, use default value of 5 euro

discounted_items = "steak eggs milk".split()
basket_items = "olive cheese pasta corn eggs ramen pepper".split()

sum = 0

for item in basket_items:
  // actual_price = ??? # use dict.get method to use default value

  if item in discounted_items:
    discounted_price = actual_price * 0.5
    sum = sum + discounted_price
  else:
    actual_price = ...
    sum = sum + actual_price
