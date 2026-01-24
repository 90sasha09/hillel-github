name = "1. Калькулятор"
print (name)
a = int(input("Введіть число: "))
b = int(input("Введіть число: "))
op = input("Введи операцию (+, -, *, /): ")
result = None
if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = a / b
    if b == 0:
        result = None
if result is not None:
    print (result)
print()
print()

name = "2. Перемістити елемент у списку"
print (name)
a = [3,2,5,9,8,12,4,0,7]
b = [1]
c = []
d = [15,3,20,6,2,1,9,0,5]

x = a.pop()
a.insert(0,x)

if len(b) > 1:
        x = b.pop()
        b.insert(0, x) or b.append(x)   # в ручную оставить нужное

if len(c) > 1 :
        x = c.pop()
        c.insert(0,x) or c.append(x)    # в ручную оставить нужное

x = d.pop()
d.insert(0,x)

print(a)
print(b)
print(c)
print(d)

print()
print()

name = "2.1 Перемістити елемент у списку"
print (name)
a = [3,2,5,9,8,12,4,0,7]
b = [1]
c = []
d = [15,3,20,6,2,1,9,0,5]
op = input("Введите операцию (+, -): ")  # (a.insert "+" ; a.append = "-")

if len(a):
    if op == "+":
       x = a.pop()
       a.insert(0,x)
    elif op == "-":
        x = a.pop(0)
        a.append(x)
if len(b):
    if op == "+":
        x = b.pop()
        b.insert(0,x)
    elif op == "-":
        x = b.pop(0)
        b.append(x)
if len(c):
    if op == "+":
        x = c.pop()
        c.insert(0,x)
    elif op == "-":
        x = c.pop(0)
        c.append(x)
if len(d):
    if op == "+":
        x = d.pop()
        d.insert(0,x)
    elif op == "-":
        x = d.pop(0)
        d.append(x)

print(a)
print(b)
print(c)
print(d)

print()
print()
print()
name = "3. Розділити один список на два списки"
print (name)
a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 3]
c = [1, 2, 3, 4, 5]
d = [1]
e = []

mid = (len(a) + 1) // 2
first_half = a[:mid]
second_half = a[mid:]
print([first_half, second_half])

mid = (len(b) + 1) // 2
first_half = b[:mid]
second_half = b[mid:]
print([first_half, second_half])

mid = (len(c) + 1) // 2
first_half = c[:mid]
second_half = c[mid:]
print([first_half, second_half])

mid = (len(d) + 1) // 2
first_half = d[:mid]
second_half = d[mid:]
print([first_half, second_half])

mid = (len(e) + 1) // 2
first_half = e[:mid]
second_half = e[mid:]
print([first_half, second_half])
