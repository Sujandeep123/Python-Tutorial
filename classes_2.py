# We enter bank customer name, amount, year of deposit
# We return compounding interest at the current time.
# We can save the data to a file.


# define Customer class
# define a function that calculates compounding interest for each customers
# saves the data into a file

class Customer :
  def __init__(self, first_name, last_name, amount, interval, interest):
    self.first_name = first_name
    self.last_name = last_name
    self.amount = amount
    self.interval = interval
    self.interest = interest

  def full_name(self):
    return f"{self.first_name} {self.last_name}"

  # 1000 @ 10 % per annum for 5 years
  # interest = PTR/100
  def simple_interest(self):
    interest = (self.amount * self.interval * self.interest) / 100
    return interest

  def compound_interest(self):
    pass

# list of customers
customers = []

answer = input('Enter user details (y/n): ')

while (answer == 'y'):
  name = input('Enter user name: ').split()
  first_name, last_name = name
  infos = input('Enter deposit information [amount, interval, interest rate]: ').split()
  amount = int(infos[0])
  interval = int(infos[1])
  interest = int(infos[2])

  customer = Customer(first_name, last_name, amount, interval, interest)
  customers.append(customer)

  answer = input('Enter user details (y/n): ')

# prompt user for file_name
file = open('my output.txt', 'w')

for customer in customers:
  # print P, T, R information
  # write p, T, R into file
  file.write(customer.full_name() + '\n')
  file.write(f'Interest amount: {customer.simple_interest()}\n')
