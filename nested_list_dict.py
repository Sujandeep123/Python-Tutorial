#%%

# Nested Array

full_name = [
  ['Sujan', 'Shrestha'],
  ['Pratuat', 'Amatya']
]

# for name in full_name:
#   for n in name:
#     print(n)

# Nested Dictionary

shop_items = {
  'electronics' : {
    'tv' : 5,
    'ps4' : 2
  },
  'sports' : {
    'basketball': 20,
    'football' : 30
  }
}

for key, value in shop_items.items():
  print(f"> {key}")

  for k, v in value.items():
    print(f'>> {k} : {v}')


#%%
# Array inside dictionary

shop_items = {
  'electronics' : ['ps4', 'tv'],
  'sports' : ['cricket', 'tennis']
}

for key, value in shop_items.items():
  print(f"> {key}")

  for k in value:
    print(f'>> {k}')
