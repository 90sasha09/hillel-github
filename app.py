from flask import Flask, render_template, request, redirect
from datetime import datetime
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"


class Person:
    def __init__(self, first_name, last_name="", middle_name="", birth_date="", death_date="", gender=""):
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.middle_name = middle_name.strip()
        self.birth_date = self.parse_date(birth_date)
        self.death_date = self.parse_date(death_date) if death_date else None
        self.gender = gender.lower()

    def parse_date(self, date_str):
        formats = ["%d.%m.%Y", "%d/%m/%Y", "%d-%m-%Y"]
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        raise ValueError("Неверный формат даты")

    def age(self):
        end = self.death_date if self.death_date else datetime.now()
        age = end.year - self.birth_date.year
        if (end.month, end.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def full_name(self):
        return " ".join(filter(None, [self.first_name, self.last_name, self.middle_name]))

    def gender_text(self):
        if self.gender == "m":
            return "мужчина"
        elif self.gender == "f":
            return "женщина"
        return "неизвестно"


def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    people = []
    for item in data:
        people.append(Person(**item))
    return people


def save_data(people):
    data = []
    for p in people:
        data.append({
            "first_name": p.first_name,
            "last_name": p.last_name,
            "middle_name": p.middle_name,
            "birth_date": p.birth_date.strftime("%d.%m.%Y"),
            "death_date": p.death_date.strftime("%d.%m.%Y") if p.death_date else "",
            "gender": p.gender
        })

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


@app.route("/")
def index():
    query = request.args.get("q", "").lower()
    people = load_data()

    if query:
        people = [p for p in people if query in p.full_name().lower()]

    return render_template("index.html", people=people, query=query)


@app.route("/add", methods=["POST"])
def add():
    try:
        person = Person(
            request.form["first_name"],
            request.form.get("last_name", ""),
            request.form.get("middle_name", ""),
            request.form["birth_date"],
            request.form.get("death_date", ""),
            request.form["gender"]
        )

        people = load_data()
        people.append(person)
        save_data(people)

    except Exception as e:
        return f"Ошибка: {e}"

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
