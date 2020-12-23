#%% ========== Voting ========== %%#

candidates =      ['pkd', 'kpo', 'sbd', 'rms']
candidate_vote =  [ 0,     0,     0,     0]

votes = ['pkd', 'kpo', 'sbd', 'kpo', 'sbd', 'sbd', 'sbd', 'pkd', 'rms', 'sbd', 'rms']

for vote in votes:
  index = candidates.index(vote)
  candidate_vote[index] = candidate_vote[index] + 1

print(candidate_vote)

#%% ==========  ========== %%#

cmds = ['sum', 4, 5, 'sub', 5, 2, 'mul', 5, 10]
output_list = []

for index, element in enumerate(cmds):
  if type(element) == str:
    if element == 'sum':
      pass
      # a = ?
      # b = ?
      output_list.append(a + b)
      # add next two element
      # add result to output_list
    elif element == 'sub':
      pass
      # subtract next two element
      # add result to output_list
    elif element == 'mul':
      pass
      # multiply next two element
      # add result to output_list

print(output_list)

#%% ==========  ========== %%#


def sum(input_list):
  return sum(input_list)


def mul(input_list):
  product = 1

  for input in input_list:
    product = product * input

  return product

cmds = ['sum', 4, 6, 7, 'sum', 5, 9, 23, 45, 67, 'mul', 32, 6, 7, 9, 'mul', 3, 4]


results = []
temp_list= []
last_cmd = None

for index, cmd in enumerate(cmds):

  if cmd is string
    last_cmd = cmd
    temp_list = []
  else if cmd is number
    temp_list.append(cmd)

  if index == len(cmds)-1 or type(cmds[index+1])
    if last_cmd == 'sum':
      results.append(sum(temp_list))
    elif last_cmd == 'mul':
      results.append(mul(temp_list))


values @ index, cmd, last_cmd, temp_list, results




























#%% ==========  ========== %%#

# Given two sorted numeric list, create a third sorted list which incorporates all value from previous two arrays.

list_1 = [1, 4, 6, 7]
list_2 = [1, 5, 6, 8]

output_list = [1, 1, 4, 5, 6, 6, 7, 8]


list_1 = list_1.reverse()
list_2 = list_2.reverse()

output_list = []

while len(list_1) != 0 and len(list_2) != 0:
  # if list_1[0]