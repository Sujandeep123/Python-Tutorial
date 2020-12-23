input_array = [int(x) for x in '61 46 80 77 28 1 57 86 73 56 60 4 83 100 14 2 69 85 80 3 34 38 67 77 13 77 99 34 77 94 47 83 39 85 75 96 37 14 57 24 62 19 60 12 23 68 6 85 71 46 27 91 50 86 100 76 12 32 38 38 21 90 34 39 3 52 14 4 2 68 32 91 33 86 66 10 3 79 27 91 28 29 34 65 15 83 31 91 8 85 48 35 31 94 87 13 48 23 75 29'.split()]

#%% ========== Ex 1 ========== %%#

# Given a list of integers, build a new list containing sum of consecutive 5 numbers.

# Consider input array length is always multiple of 5

# Example:
# input_array = [1,2,3,4,5,6,7,8,9,0,6,4,3,70,56]

# output_array = [15, 30, 139]

# Explanation:
# sum of first batch of numbers [1,2,3,4,5] = 15
# sum of second batch of numbers [6,7,8,9,0] = 30
# sum of third batch of numbers [6,4,3,70,56] = 139

for index in range(10):
  print(index)

index = 0
while index < len(input_array)/5:
  start_index = index * 5
  end_index = start_index + 5

  print(sum(input_array[start_index:end_index]))

  index += 1



#%% ========== Ex 2 ========== %%#

# Given a list of integers, build new list of numbers that occurs only once in the list.

# input_array = [5, 4, 3, 6, 4, 6, 4, 2]
# output_array = [5, 3, 2], list of numbers that occurs only once
