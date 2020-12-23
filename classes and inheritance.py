#%%
array_scores = [
  ['Student A', 10, 12, 13, 14],
  ['Student B', 12, 45, 56],
  ['Student C', 122, 245]
]

for element in array_scores:
  for sub_element in element:
    print(sub_element)


#%%

dict_scores = {
  'student A' : {
    'name' : 'Sujan',
    'math' : 10,
    'optional math' : 12
  },
  'student B' : {
    'name' : 'Shrabya',
    'math' : 10,
    'geography' : 12
  },
  'student C' : {
    'name' : 'Sunita',
    'english' : 10,
    'science' : 12
  }
}

for key, value in dict_scores.items():
  for k, v in value.items():
    print(k, '>>>', v)


#%%

# Inheritance

## Normal Class
class Student:
  def __init__(self, name, address, scores):
    self.name = name
    self.address = address
    self.scores = scores

  def full_details(self):
    return (f"Name: {self.name} \nAddress: {self.address}\n")


class Employee:
  def __init__(self, name, address, department, classes):
    self.name = name
    self.address = address
    self.department = department
    self.classes = classes

  def full_details(self):
    return (f"Name: {self.name} \nAddress: {self.address}\n")

class Staff:
  def __init__(self, name, address, workhour):
    self.name = name
    self.address = address
    self.workhour = workhour

  def full_details(self):
    return (f"Name: {self.name} \nAddress: {self.address}\n")


print(sujan.full_details())
print(pratyut.full_details())
print(anyone.full_details())

#%%
## Inherited Classes


# Parent class
class Person:
  def __init__(self, name, address):
    self.name = name
    self.address = address

  def full_details(self):
    print(f"Name: {self.name} \nAddress: {self.address}\n")


# Child class
class Student(Person):  ## Student inherits from Person

  def __init__(self, name, address, scores):
    super().__init__(name, address)
    self.scores = scores

  def student_full_details(self):
    super().full_details()

    for key, value in self.scores.items():
      print(f"{key} : {value}")


class Teacher(Person):  ## Student inherits from Person

  def __init__(self, name, address, subjects):
    super().__init__(name, address)
    self.subjects = subjects

  def full_details(self):
    super().full_details() ## your choice
    print(self.subjects)


child_obj = Student('Sujan Shrestha', 'Chakupaat', {'Math' : '8 am to 10 am', 'Science' : '12 am to 2pm'})
teacher_obj = Teacher('Sujana Shrestha', 'Chakupaat', "Math : 8 am to 10 am,\nScience : 12 am to 2pm")
teacher_obj.teacher_full_details()
child_obj.student_full_details()


# Class -> summation of data(attributes) + functions (methods)

# Inhertances addresses the problem of redundancies, splits what is common and what is different
# extract commonalities to parent class (super-class)
# extract differences to child class (sub-class)
# sub-class reuses attributes from super-class
# sub-class reuses functions from super-class
