def find_unique_value(numbers):
    for num in numbers:
        if numbers.count(num) == 1:
            return num
    return None

print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3, 5, 5]))
print(find_unique_value([5, 5, 5, 2, 2, 0.5]))


