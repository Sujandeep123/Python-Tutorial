items = "olive cheese steak cornflakes pasta corn beans eggs milk".split()
prices = [1.99, 1.69, 4.5, 2.5, .55, 1.69, 1.4, 1.29, .79]

discounted_items = "steak eggs milk"
basket_items = "olive cheese pasta corn eggs"


sum = 0

for item in basket_items:
  // actual_price = ???

  if item in discounted_items:
    discounted_price = actual_price * 0.5
    sum = sum + discounted_price
  else:
    actual_price = ...
    sum = sum + actual_price
