DB_HOST = "postgres_db"
DB_NAME = "postgres" 
DB_USER = "postgres" 
DB_PASS = "postgres"

import psycopg2

conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS)

cur = conn.cursor()

cur.execute("CREATE TABLE createdwithpython (id SERIAL PRIMARY KEY, name VARCHAR)")
cur.execute("INSERT INTO createdwithpython (name) VALUES(%s)", ("zxcvbnm",) )
cur.execute("select * from createdwithpython where id=6;")
print(cur.fetchall())

conn.commit()
conn.close()