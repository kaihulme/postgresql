from db.connection import connect

cur = connect()

query = "SELECT * FROM payment"
cur.execute(query)

print(cur.fetchone())

