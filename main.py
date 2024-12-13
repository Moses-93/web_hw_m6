from db.connect import create_connection, my_db
from db.query import execute_sql


queries = [f"queries/query_{i}.sql" for i in range(1, 11)]

for i, query in enumerate(queries, start=1):
    with open(query) as file:
        sql_query = file.read()
        with create_connection(my_db) as conn:
            res = execute_sql(conn, sql_query, fetch=True)
            print(f"Results for query {i}:\n" + "-" * 30)
            for row in res:
                print(f"{row}")
            print("\n")
