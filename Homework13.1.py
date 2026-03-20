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
        if isinstance(student, Student):
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


# Приклад використання:
group = Group("A1")

s1 = Student("Ivan", "Ivanov", 20, "S001")
s2 = Student("Petro", "Petrenko", 21, "S002")
s3 = Student("Olena", "Shevchenko", 19, "S003")

group.add_student(s1)
group.add_student(s2)
group.add_student(s3)

print(group)

found = group.find_student("Petrenko")
print("Found:", found.info() if found else "Not found")

group.remove_student("Ivanov")
print("\nAfter removal:")
print(group)