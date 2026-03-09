
def sequence_generator(x):
    return x ** 2

def some_gen(begin, end, func):
 current = begin
 for _ in range(end):
        yield current
        current = func(current)

from inspect import isgenerator

gen = some_gen(2, 4, sequence_generator)
print(isgenerator(gen))
print(list(gen))
print('OK')

