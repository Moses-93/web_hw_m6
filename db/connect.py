from contextlib import contextmanager
import sqlite3

my_db = "university.db"

@contextmanager
def create_connection(my_db):
    conn = sqlite3.connect(my_db)
    yield conn
    conn.rollback()
    conn.close()