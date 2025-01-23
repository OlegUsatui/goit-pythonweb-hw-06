from db import session 
from models import Base
from faker import Faker
from models import Student, Group, Teacher, Subject, Grade
import random

PREDEFINED_SUBJECTS = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "Biology",
    "History",
    "Geography",
    "English",
    "Computer Science",
    "Physical Education",
    "Art"
]

Base.metadata.drop_all(bind=session.get_bind())
Base.metadata.create_all(bind=session.get_bind())

fake = Faker()

groups = [Group(name=f"Group {i+1}") for i in range(3)]
session.add_all(groups)

teachers = [Teacher(name=fake.name()) for _ in range(3)]
session.add_all(teachers)

subjects = [Subject(name=subject, teacher=random.choice(teachers)) for subject in PREDEFINED_SUBJECTS]
session.add_all(subjects)

students = []
for _ in range(30):
    student = Student(name=fake.name(), group=groups[fake.random_int(0, 2)])
    session.add(student)
    students.append(student)

for student in students:
    for subject in subjects:
        grade = Grade(grade=fake.random_int(1, 10), received_at=fake.date(), student=student, subject=subject)
        session.add(grade)

session.commit()

print("База даних успішно заповнена!")
