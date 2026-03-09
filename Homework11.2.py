def generate_cube_numbers(end):
    n = 2
    while True:
        cube = n ** 3
        if cube >= end:
            return
        yield cube
        n += 1

from inspect import isgenerator

gen = generate_cube_numbers(1)
print(isgenerator(gen))
print(list(generate_cube_numbers(10)))
print(list(generate_cube_numbers(100)))
print(list(generate_cube_numbers(1000)))