cur_len, max_len = 0, 0
previous_char = "x"

for char in input():
    if char != previous_char:
        max_len = max(max_len, cur_len)
        cur_len = 0
        previous_char = char
    cur_len += 1

max_len = max(max_len, cur_len)
print(max_len)
