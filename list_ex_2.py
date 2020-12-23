#%%

days_of_week = "sunday monday tuesday wednesday thursday friday saturday".split()

# Scenario 1: we have keys, we need to access values
index = 0
print(days_of_week[index])

# Scenario 2: we have values, we need index
print(days_of_week.index('wednesday'))


#%%

items = "olive cheese steak cornflakes pasta corn beans eggs milk".split()

prices = [1.99, 1.69, 4.5, 2.5, .55, 1.69, 1.4, 1.29, .79]

discounted_items = "steak eggs milk".split()
basket_items = "olive cheese pasta corn eggs".split()
sum = 0
for item in basket_items:
  index_of_items = items.index(item)
  actual_price = prices[index_of_items]
  if item in discounted_items:
    discounted_price = actual_price * 0.5
    sum = sum + discounted_price
  else:
    sum = sum + actual_price
print(sum)

#%% using dictionary

item_prices = {
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

sum = 0
for item in basket_items:
  actual_price = item_prices[item]
  if item in discounted_items:
    discounted_price = actual_price * 0.5
    sum = sum + discounted_price
  else:
    sum = sum + actual_price

print(sum)
