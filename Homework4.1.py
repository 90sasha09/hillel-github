name = "ДЗ 4.1. Перемістити всі нулі до кінця списку"
print(name)
a = [0, 1, 0, 12, 3]
b = [0]
c = [1, 0, 13, 0, 0, 0, 5]
d = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

a.sort(key = lambda x : x == 0)
b.sort(key = lambda x : x == 0)
c.sort(key = lambda x : x == 0)
d.sort(key = lambda x : x == 0)
print(a)
print(b)
print(c)
print(d)

