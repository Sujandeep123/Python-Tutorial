#%%
class Company:
  def __init__(self, name, address, contact):
    self.name = name
    self.address = address
    self.contact = contact

  def greet(self):
    print ("hello", self.name, self.address)

#%%

c = Company('TATA', 'India', '123')
d = Company('AIG', 'US', '1234')

c.greet()
d.greet()


# Section 2
## Variable Scope

# 1. Local variable : scope is within function definition (current scope)
# 2. Instance variable : scope is within object or instance
# 3. Class variable
# 4. Global variable
