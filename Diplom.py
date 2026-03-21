from datetime import datetime
import json

class Person:
    def _init_(self, first_name, last_name="", middle_name="", birth_date="", death_date="", gender=""):
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.middle_name = middle_name.strip()
        self.birth_date = self.parse_date(birth_date)
        self.death_date = self.parse_date(death_date) if death_date else None
        self.gender = gender.lower()

    def parse_date(self, date_str):
        formats = ["%d.%m.%Y", "%d %m %Y", "%d/%m/%Y", "%d-%m-%Y"]
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except:
                continue
        raise ValueError("Невірний формат дати")

    def calculate_age(self):
        end_date = self.death_date if self.death_date else datetime.now()

        age = end_date.year - self.birth_date.year
        if (end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def full_name(self):
        return " ".join(filter(None, [self.first_name, self.last_name, self.middle_name]))

    def gender_text(self):
        return "чоловік" if self.gender == "m" else "жінка"

    def _str_(self):
        age = self.calculate_age()
        birth = self.birth_date.strftime("%d.%m.%Y")

        if self.death_date:
            death = self.death_date.strftime("%d.%m.%Y")
            return f"{self.full_name()} {age} років, {self.gender_text()}. Народився {birth}. Помер: {death}."
        else:
            return f"{self.full_name()} {age} років, {self.gender_text()}. Народився {birth}."


class Database:
    def _init_(self):
        self.people = []

    def add_person(self):
        try:
            first = input("Ім'я: ")
            last = input("Прізвище (можна пусто): ")
            middle = input("По батькові (можна пусто): ")
            birth = input("Дата народження: ")
            death = input("Дата смерті (можна пусто): ")
            gender = input("Стать (m/f): ")

            person = Person(first, last, middle, birth, death, gender)
            self.people.append(person)

            print("✅ Запис додано")
        except Exception as e:
            print("❌ Помилка:", e)

    def search(self, query):
        query = query.lower()
        results = []

        for person in self.people:
            if query in person.full_name().lower():
                results.append(person)

        return results

    def save_to_file(self, filename="data.json"):
        data = []

        for p in self.people:
            data.append({
                "first_name": p.first_name,
                "last_name": p.last_name,
                "middle_name": p.middle_name,
                "birth_date": p.birth_date.strftime("%d.%m.%Y"),
                "death_date": p.death_date.strftime("%d.%m.%Y") if p.death_date else "",
                "gender": p.gender
            })

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("💾 Збережено")

    def load_from_file(self, filename="data.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.people = []

            for item in data:
                p = Person(
                    item["first_name"],
                    item["last_name"],
                    item["middle_name"],
                    item["birth_date"],
                    item["death_date"],
                    item["gender"]
                )
                self.people.append(p)

            print("📂 Дані завантажено")
        except Exception as e:
            print("❌ Помилка:", e)


def main():
    db = Database()

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Додати людину")
        print("2. Пошук")
        print("3. Зберегти у файл")
        print("4. Завантажити з файлу")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            db.add_person()

        elif choice == "2":
            query = input("Введіть для пошуку: ")
            results = db.search(query)

            if results:
                for p in results:
                    print(p)
            else:
                print("Нічого не знайдено")

        elif choice == "3":
            db.save_to_file()

        elif choice == "4":
            db.load_from_file()

        elif choice == "0":
            print("👋 Вихід")
            break

        else:
            print("❌ Невірний вибір")


if "_name_" == "_main_":
    main()
