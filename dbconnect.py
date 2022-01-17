import psycopg2 as pg2
import secret

conn = pg2.connect(
	host=secret.host,
	database=secret.db, 
	user=secret.user, 
	password=secret.password
)

cur = conn.cursor()

cur.execute("SELECT * FROM payment")

fetched = cur.fetchone()
print(fetched)

