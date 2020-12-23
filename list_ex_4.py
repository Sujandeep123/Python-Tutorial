# A voting was conducted to elect next PM of the nation. The votes are saved in an list. Count the number of votes each candidate got and determine the winner.

# candidates = {
#   'KP Oli' : 'kpo',
#   'PK Dahal' : 'pkd',
#   'SB Deuba' : 'sbd',
#   'R Mishra' : 'rms'
# }

votes = ['pkd', 'kpo', 'sbd', 'kpo', 'sbd', 'sbd', 'sbd', 'pkd', 'rms', 'sbd', 'rms']

#%% Using lists

candidates = ['kpo', 'pkd', 'sbd', 'rms']
vote_count = [5, 20, 10, 30]

# max_value = max(vote_count)
# max_value_index = vote_count.index(max_value)
# winner = candidates[max_value_index]

print("Vote Count: ", vote_count)

for vote in votes:
  print('-'*50)
  index = candidates.index(vote)
  vote_count[index] = vote_count[index] + 1

  print("Vote: ", vote)
  print("Index: ", index)
  print("Vote Count: ", vote_count)

#%% Using dictionary

vote_count = {
  'kpo' : 0,
  'pkd' : 0,
  'sbd' : 0,
  'rms' : 0
}

print("Vote Count: ", vote_count)

for vote in votes:
  print('-'*50)
  vote_count[vote] = vote_count[vote] + 1

  print("Vote: ", vote)
  print("Vote Count: ", vote_count)
#%%
