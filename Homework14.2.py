
class GroupLimitError(Exception):
    pass

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)
        return False


    def __hash__(self):
        return hash(str(self))



class Group:
    def __init__(self, name):
        self.name = name
        self.group = set()

    def add_student(self, student):
        if not isinstance(student, Student):
            return

        if len(self.group) >= 10:
            raise GroupLimitError("У групі не може бути більше 10 студентів")

        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        if not self.group:
            return f"Group {self.name} is empty"

        students_list = '\n'.join(str(st) for st in self.group)
        return f"Group: {self.name}\n{students_list}"



if __name__ == "__main__":
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

    gr = Group('PD1')

    try:
        gr.add_student(st1)
        gr.add_student(st2)

        print(gr)

        # ✔ Перевірки
        assert gr.find_student('Jobs') == st1
        assert gr.find_student('Jobs2') is None

        gr.delete_student('Taylor')

        print("\nAfter delete:")
        print(gr)

        # ✔ Перевірка ліміту (додамо ще 9 студентів)
        for i in range(9):
            gr.add_student(Student('Male', 20, f'Name{i}', f'Last{i}', f'ID{i}'))

        # Це викличе виняток
        gr.add_student(Student('Male', 22, 'Extra', 'Student', 'ID999'))

    except GroupLimitError as e:
        print("\nПомилка:", e)

