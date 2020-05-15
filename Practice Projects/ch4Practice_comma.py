# Solution 1, ugly
def oxford_comma(s):
    if s:
        return_string = ""
        s.insert(-1, 'and')
        for x in s[:-2]:
            return_string += x + ', '
        return return_string + s[-2] + ' ' + s[-1]

# solution 2, better
def comma_code(s):
    if s:
        begin, end = s[:-1], s[-1]
        return f"{', '.join(begin)} and {end}"

spam = ['cat', 'dog', 'rat', 'snake']

print(comma_code(spam))
