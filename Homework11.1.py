def prime_generator(n):
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
from inspect import isgenerator

gen = prime_generator(1)

print(isgenerator(gen))
print(list(prime_generator(10)))
print(list(prime_generator(15)))
print(list(prime_generator(29)))