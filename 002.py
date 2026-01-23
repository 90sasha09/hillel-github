age = input("What is your age? ")

if age.isdigit() and int(age) < 0:
        age = int(age)


if age <= 5:
        print("Milk")
elif age <= 12:
        print("Juice")
elif age <= 18:
        print("Soda")
elif age <= 100:
        print("Coffe")
else:
    print("Invalid age")



