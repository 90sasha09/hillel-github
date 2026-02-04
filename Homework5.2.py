name = "ДЗ 5.2 Модифікувати калькулятор"
print(name)
while True:
    a = int(input("Введіть число: "))
    b = int(input("Введіть число: "))
    op = input("Введи операцию (+, -, *, /): ")
    result = None
    if op == "+":
         result = a + b
    elif op == "-":
             result = a - b
    elif op == "*":
           result = a * b
    elif op == "/":
           result = a / b
    if b == 0:
           result = None
    if result is not None:
     print(result)
    answer = input("Начать заного ? (yes / no): ").strip().lower()
    if answer == "yes":
            continue
    elif answer == "no":
     print("bye")
     break
    else:
     print("'yes' or 'no'")




