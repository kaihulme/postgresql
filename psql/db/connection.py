import psycopg2 as pg2
import secret


def connect():
	conn = pg2.connect(
		host=secret.host,
		database=secret.db, 
		user=secret.user, 
		password=secret.password
	)
	return conn.cursor()

