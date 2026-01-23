name1 = "1. Квадрат числа"
print(name1)
number1 = int(input("Введіть число: "))
square =number1 * number1
print(square)
print()
print()
name2 = "2. Середнє трьох чисел"
print(name2)
number_2a, number_2b, number_3c = map(int, input("Введіть три числа через кому: ").split(','))
sum = (number_2a + number_2b + number_3c) / 3
print(sum)
print()
print()
name3 = "3. Перетворення хвилин у години"
print(name3)
name03 = "години"
name030 = "хвилин"
number_3 = int(input("Введіть кількість хвилин: "))
sum1 = int(number_3 / 60)
sum2 = int(sum1 * 60)
sum3 = int(number_3 - sum2)
print(sum1, name03, sum3, name030)
print()
print()
name4 = "4. Розрахунок знижки"
print(name4)
number_4a = int(input("Введіть ціну: "))
number_4b = int(input("Введіть знижку (%): "))
print((number_4a - (number_4a / 100)*number_4b))
print()
print()
name5 = "5. Остання цифра числа"
print(name5)
number_5 = int(input("Enter a number: "))
print(number_5 % 10)
print()
print()
name6 = "6. Периметр прямокутника"
print(name6)
a = int(input("Введіть довжину: "))
b = int(input("Введіть ширину: "))
sum4 = int(a + b) * 2
print(sum4)
print()
print()
name7 = "7. Виведення числа в стовпчик"
print(name7)
number_7 = int(input("Введіть число: "))
print(number_7 // 1000)
print((number_7 // 100) % 10)
print((number_7 // 10) % 10)
print(number_7 % 10)
print()