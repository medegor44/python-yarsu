import psycopg

with psycopg.connect('dbname=todo user=postgres password=1 host=localhost port=5432') as conn:
    with conn.cursor() as cur:
        for t in cur.execute("SELECT * FROM items").fetchall():
            print(t)
            t = cur.fetchone()