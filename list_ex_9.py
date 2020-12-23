#%% ==========  ========== %%#

test_a = "GGATCCGGAAAATTTGGGGAAG"

compressed_string = []
last_char = None
last_char_count = 0


# edge cases

# for i, char in enumerate(test_a)
#   if char != last_char //  >> "insert_event" <<
#     if i != 0
#       insert last_char
#       if last_char_count > 1
#         insert last_char_count
#     last_char = char
#     last_char_count = 1
#   else // if char == last_char
#     last_char_count += 1
#
#   if end of iteration: // this is edge-case, also trigger >> "insert-event" <<
#     insert last_char
#     if last_char_count > 1
#       insert last_char_count
