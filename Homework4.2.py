name = "ДЗ 4.2 Знайти суму елементів із парними індексами"
print(name)
a = [0, 1, 7, 2, 4, 8]
b =[1, 3, 5]
c =[6]
d = []

def calc(lst):
    return sum(lst[::2]) *lst[-1] if lst else 0

print(calc(a))
print(calc(b))
print(calc(c))
print(calc(d))





