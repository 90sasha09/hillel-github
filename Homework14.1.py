class GroupLimitError(Exception):
    pass


class Human:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def info(self):
        return f"Human: {self.first_name} {self.last_name}, Age: {self.age}"


class Student(Human):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id

    def info(self):
        return f"Student: {self.first_name} {self.last_name}, Age: {self.age}, ID: {self.student_id}"


class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if not isinstance(student, Student):
            return

        if len(self.students) >= 10:
            raise GroupLimitError("У групі не може бути більше 10 студентів")

        self.students.append(student)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def remove_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.students.remove(student)
            return True
        return False

    def __str__(self):
        if not self.students:
            return f"Group {self.name} is empty"

        result = f"Group {self.name}:\n"
        for student in self.students:
            result += student.info() + "\n"
        return result


# 🔹 Тестування
group = Group("A1")

try:
    for i in range(11):  # пробуємо додати 11 студентів
        student = Student(f"Name{i}", f"Surname{i}", 20, f"ID{i}")
        group.add_student(student)
        print(f"Added student {i}")

except GroupLimitError as e:
    print("Помилка:", e)

print("\nСклад групи:")
print(group)

