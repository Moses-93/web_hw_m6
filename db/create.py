import sqlite3
from . import connect, query


table_groups = """
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
"""

table_teachers = """
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
"""

table_subjects = """
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    teacher_id INTEGER NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
);
"""

table_students = """
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    group_id INTEGER NOT NULL,
    FOREIGN KEY (group_id) REFERENCES groups (id)
);
"""

table_grades = """
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    subject_id INTEGER NOT NULL,
    grade INTEGER NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
);
"""


with connect.create_connection(connect.my_db) as conn:
    tables = [table_groups, table_teachers, table_subjects, table_students, table_grades]
    for i, table in enumerate(tables, start=1):
        try:
            query.execute_sql(conn, table)
            print(f"Table {i} created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating table {i}: {e}")
    

