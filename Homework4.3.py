name = "ДЗ 4.3. Список із 3 елементів"
print(name)
a = [1, 2, 3, 4, 5, 6, 7, 9]
b = [1, 1, 2, 1]
c = [6, 3, 7]

def make_list(lst):
    return [lst[0], lst[2], lst[-2]]
print(make_list(a))
print(make_list(b))
print(make_list(c))
