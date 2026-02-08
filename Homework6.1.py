#"a-c" -> abc
#"a-a" -> a
#"s-H" -> stuvwxyzABCDEFGH
#"a-A" -> abcdefghijklmnopqrstuvwxyzA



import string

letters = string.ascii_letters
start, end = input().split('-')
i1 = letters.index(start)
i2 = letters.index(end)
print(letters[i1:i2 + 1])


