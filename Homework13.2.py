class Counter:
    def __init__(self, min_value=0, max_value=10, current_value=None):
        self.min_value = min_value
        self.max_value = max_value

        if current_value is None:
            self.current_value = min_value
        else:
            if not (min_value <= current_value <= max_value):
                raise ValueError("Початкове значення поза межами діапазону")
            self.current_value = current_value

    def set_min(self, min_value):
        if min_value > self.max_value:
            raise ValueError("Мінімум не може бути більшим за максимум")
        self.min_value = min_value
        if self.current_value < self.min_value:
            self.current_value = self.min_value

    def set_max(self, max_value):
        if max_value < self.min_value:
            raise ValueError("Максимум не може бути меншим за мінімум")
        self.max_value = max_value
        if self.current_value > self.max_value:
            self.current_value = self.max_value

    def set_current(self, value):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError("Значення поза допустимими межами")
        self.current_value = value

    def step_up(self):
        if self.current_value >= self.max_value:
            raise ValueError("Досягнуто максимуму")
        self.current_value += 1

    def step_down(self):
        if self.current_value <= self.min_value:
            raise ValueError("Досягнуто мінімуму")
        self.current_value -= 1

    def get_value(self):
        return self.current_value

    def __str__(self):
        return f"Counter(value={self.current_value}, min={self.min_value}, max={self.max_value})"



counter = Counter(min_value=0, max_value=5, current_value=2)

print(counter)

counter.step_up()
print(counter.get_value())

counter.step_down()
print(counter.get_value())


try:
    counter.set_current(5)
    counter.step_up()
except ValueError as e:
    print("Помилка:", e)

try:
    counter.set_current(0)
    counter.step_down()
except ValueError as e:
    print("Помилка:", e)

