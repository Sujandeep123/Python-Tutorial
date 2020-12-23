customers = ["Iliana Windler LLD", "Rep. Bryanna Schuppe", "Noe Hills", "Felton Jacobs", "Augustus Parisian", "Gov. Bernetta Nader", "Sen. Katrice Ritchie", "Marchelle Treutel DDS", "Sammy Frami", "Ms. Dwayne Bradtke"]

payments = [[68, 74, 50, 93, 76, 74, 98, 56, 72, 47],
[69, 63, 55, 55, 87, 55, 91, 55, 69, 61],
[96, 84, 77, 44, 93, 40, 79, 62, 85, 84],
[76, 54, 89, 88, 67, 42, 62, 87, 97, 99],
[71, 92, 87, 74, 98, 73, 76, 85, 63, 58]]



# Option 1
record = [
  ['Iliana Windler LLD', [68, 69, 96, 76, 71]],
  ['Rep. Bryanna Schuppe', [74, 63, 84, 54, 92]],
  .....
]

record = {
  'Ilian W LLD' : [68, 69, 96, 76, 71],
  'sujan'  : []
}

customers = ["Iliana Windler LLD", "Rep. Bryanna Schuppe", "Noe Hills", "Felton Jacobs", "Augustus Parisian", "Gov. Bernetta Nader", "Sen. Katrice Ritchie", "Marchelle Treutel DDS", "Sammy Frami", "Ms. Dwayne Bradtke"]
payments = [
  [68, 69, 96, 76, 71],
  []
]

customers.sort()

for customer in customers:
  print(customer, customer_payment_history)
