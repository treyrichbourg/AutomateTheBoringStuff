message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
#example of how setdefault method will add the key "character" to the dictionary 'count'
for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)