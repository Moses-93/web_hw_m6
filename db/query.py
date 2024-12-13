import sqlite3
from typing import Optional, Tuple, Any


def execute_sql(
        conn: sqlite3.Connection, 
        query: str, 
        params: Optional[Tuple[Any, ...]] = None, 
        fetch: bool = False
            ) -> Optional[list[tuple]]:
    """
    Універсальна функція для виконання SQL-запитів.
    - `fetch=True`: повертає результати для SELECT-запитів.
    - `fetch=False`: виконує запит без повернення результатів.
    """
    try:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        if fetch:  # Якщо треба отримати дані
            result = cursor.fetchall()
            print(f"Query fetched: {query} | Params: {params}", end="\n\n")
            return result
        else:  # Якщо це DML чи DDL запит
            conn.commit()
            print(f"Query executed: {query} | Params: {params}", end="\n\n")
            return None
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        cursor.close()
