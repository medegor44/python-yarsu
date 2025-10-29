import mssql_python

with mssql_python.connect('SERVER=localhost;PORT=1433;DATABASE=todo;UID=sa;PWD=1234qwE?;TrustServerCertificate=yes') as conn:
    with conn.cursor() as cur:
        for t in cur.execute("SELECT * FROM items").fetchall():
            print(t)
            t = cur.fetchone()