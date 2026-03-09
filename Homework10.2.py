import re

def first_word(text: str) -> str:
    match = re.search(r"[a-zA-Z']+", text)
    return match.group(0)

print(first_word("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word(".., and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))