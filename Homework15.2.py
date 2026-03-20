class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не може бути 0")
        self.a = a
        self.b = b


    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)


    def __add__(self, other):
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)


    def __sub__(self, other):
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)


    def _reduce(self):
        from math import gcd
        g = gcd(self.a, self.b)
        return self.a // g, self.b // g


    def __eq__(self, other):
        a1, b1 = self._reduce()
        a2, b2 = other._reduce()
        return a1 == a2 and b1 == b2


    def __gt__(self, other):
        return self.a * other.b > other.a * self.b


    def __lt__(self, other):
        return self.a * other.b < other.a * self.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"



f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'

f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'

f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print('OK ✅')

