import string

text = input("Введіть рядок: ")
for ch in string.punctuation:
    text = text.replace(ch, "")
words = text.split()
words = [word.capitalize() for word in words]
hashtag = "#" + "".join(words)
hashtag = hashtag[:140]
print(hashtag)


