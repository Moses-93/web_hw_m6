import random
from faker import Faker

from .connect import create_connection, my_db
from .query import execute_sql

fake = Faker()

# SQL-запити
sql_teachers = '''INSERT INTO teachers (name) VALUES (?)'''
sql_students = '''INSERT INTO students (name, group_id) VALUES (?, ?)'''
sql_groups = '''INSERT INTO groups (name) VALUES (?)'''
sql_subjects = '''INSERT INTO subjects (name, teacher_id) VALUES (?, ?)'''
sql_grades = '''INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)'''

if __name__ == '__main__':
    try:
        with create_connection(my_db) as conn:
            # Вимикаємо автокоміт для прискорення операцій
            conn.isolation_level = None
            conn.execute("BEGIN")

            # Заповнення таблиці груп
            group_names = [("Group A",), ("Group B",), ("Group C",)]
            conn.executemany(sql_groups, group_names)

            # Заповнення таблиці викладачів
            teachers = [(fake.name(),) for _ in range(5)]
            conn.executemany(sql_teachers, teachers)

            # Отримання ID викладачів
            teacher_ids = [row[0] for row in execute_sql(conn, "SELECT id FROM teachers", fetch=True)]

            # Заповнення таблиці предметів
            subjects = [("Math", random.choice(teacher_ids)),
                        ("Physics", random.choice(teacher_ids)),
                        ("Chemistry", random.choice(teacher_ids)),
                        ("Biology", random.choice(teacher_ids)),
                        ("History", random.choice(teacher_ids)),
                        ("Literature", random.choice(teacher_ids)),
                        ("Programming", random.choice(teacher_ids)),
                        ("Art", random.choice(teacher_ids))]
            conn.executemany(sql_subjects, subjects)

            # Отримання ID груп
            group_ids = [row[0] for row in execute_sql(conn, "SELECT id FROM groups", fetch=True)]

            # Заповнення таблиці студентів
            students = [(fake.name(), random.choice(group_ids)) for _ in range(50)]
            conn.executemany(sql_students, students)

            # Отримання ID студентів і предметів
            student_ids = [row[0] for row in execute_sql(conn, "SELECT id FROM students", fetch=True)]
            subject_ids = [row[0] for row in execute_sql(conn, "SELECT id FROM subjects", fetch=True)]

            # Заповнення таблиці оцінок
            grades = []
            for student_id in student_ids:
                for subject_id in subject_ids:
                    for _ in range(random.randint(5, 20)):
                        grade = random.randint(60, 100)
                        date = fake.date_this_year().isoformat()
                        grades.append((student_id, subject_id, grade, date))
            conn.executemany(sql_grades, grades)

            # Завершення транзакції
            conn.commit()
            print("The database is filled successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
