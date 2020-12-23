

#%% ==========  ========== %%#

 item_prices = [('beans', '97'),
 ('steak', '13'),
 ('corn', '85'),
 ('cornflakes', '61'),
 ('cheese', '10'),
 ('cornflakes', '24'),
 ('cheese', '1'),
 ('cheese', '7'),
 ('cornflakes', '39'),
 ('steak', '56'),
 ('beans', '82'),
 ('eggs', '82'),
 ('beans', '49'),
 ('cornflakes', '43'),
 ('steak', '75'),
 ('cornflakes', '76'),
 ('cheese', '31'),
 ('milk', '10'),
 ('cornflakes', '87'),
 ('cornflakes', '50'),
 ('cornflakes', '62'),
 ('beans', '13'),
 ('corn', '29'),
 ('cornflakes', '46'),
 ('pasta', '59'),
 ('pasta', '22'),
 ('eggs', '26'),
 ('beans', '51'),
 ('eggs', '73'),
 ('corn', '26'),
 ('beans', '25'),
 ('beans', '67'),
 ('cheese', '40'),
 ('cornflakes', '46'),
 ('olive', '6'),
 ('cornflakes', '43'),
 ('milk', '93'),
 ('beans', '20'),
 ('beans', '48'),
 ('cornflakes', '20'),
 ('beans', '51'),
 ('olive', '99'),
 ('milk', '9'),
 ('beans', '99'),
 ('beans', '31'),
 ('cornflakes', '11'),
 ('olive', '68'),
 ('cheese', '71'),
 ('steak', '79'),
 ('cornflakes', '82'),
 ('dragron furit', 200)]

# Find the minimum, maximum and average price of each item in the list

# Output:

# Beans: Min Price: 56, Max Price: 90, Average: 67
# Corn: Min Price: 56, Max Price: 90, Average: 67
# Steak: Min Price: 56, Max Price: 90, Average: 67

#%% ==========  ========== %%#


item_prices = [
  ('beans', '97'),
  ('beans', '13'),
  ('steak', '13'),
  ('steak', '85'),
  ('beans', '61')
]

prices_dict = {}

for item, price in item_prices:

  # fetch existing item_prices array or new empty array from prices dict
  prices = prices_dict.get(item, [])

  # collect current price point in existing item_prices array
  prices.append(price)

  # update prices in dictionary
  prices_dict[item]  = prices

dd =[
  ('beans', ['97', '13', '61']),
  ('steak', ['13', '85'])
]

import pdb

arr = []
for item, prices in dd:
  min_price = min(prices)
  max_price = max(prices)

  int_prices = []

  for price in prices:
    int_prices.append(int(price))

  average_price = sum(int_prices)/len(int_prices)

  print(f"{item} Min Price: {min_price}, Max Price: {max_price}, Avg Price: {average_price}")
#%%

## Bonus ##

input = [2,3,4,5]

output = []
for i in input:
  if i > 3:
    output.append(i*i)

output = [i*i for i in input if i > 3]
