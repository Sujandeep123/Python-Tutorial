#%% ========== Ex 1 ========== %%#

commands = [
  "insert 0 5 45 67",
  "insert 1 10",
  "insert 0 6",
  "remove 6",
  "append 9",
  "extend 5 6 7 8",
  "sort",
  "pop",
  "do_something 45 67 blahskdf ",
  "append 99 67 89 09",
  'print'
]

[1,2,3] + [4,5,6]

# Command Format
# 1st element: command_name
# [2,] if values exist, they are parameters to the command

my_list = []

for cmd in commands:
  cmd_list = cmd.split()
  command_name = cmd_list[0]

  if command_name == 'insert':
    index = int(cmd_list[1])
    value = int(cmd_list[2])
    my_list.insert(index, value)

  if command_name == 'extend':
    array = [int(x) for x in cmd_list[1:]]

    my_list.extend(array)

  elif command_name == 'print':
    print(my_list)

  elif command_name == 'append':
    my_list.append(int(cmd_list[1]))
