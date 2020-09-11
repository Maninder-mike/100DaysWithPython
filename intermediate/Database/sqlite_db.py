from sqlite3 import connect, Error

conn = connect("test.db")

cur = conn.cursor()

cur.execute(
		"""CREATE TABLE IF NOT EXISTS master(
		m_id INT NOT NULL,
		name TEXT NOT NULL, 
		inserted_date DATE DEFAULT CURRENT_DATE, 
		PRIMARY KEY(m_id))"""
)

cur.execute(
		"""CREATE TABLE IF NOT EXISTS slave(
		s_id INT NOT NULL,
		m_id INT NOT NULL,
		name TEXT NOT NULL, 
		inserted_date DATE DEFAULT CURRENT_TIME, 
		PRIMARY KEY(s_id),
		CONSTRAINT s_id FOREIGN KEY(m_id) REFERENCES master(m_id))"""
)

cur.execute(
		"""CREATE TABLE IF NOT EXISTS butler(
		b_id INT NOT NULL,
		m_id INT NOT NULL,
		s_id INT NOT NULL,
		name TEXT NOT NULL, 
		inserted_date DATE DEFAULT CURRENT_TIMESTAMP, 
		PRIMARY KEY(b_id),
		CONSTRAINT m_id FOREIGN KEY(m_id) REFERENCES master(m_id),
		CONSTRAINT s_id FOREIGN KEY(s_id) REFERENCES slave(s_id))"""
)

cur.execute(
	"INSERT INTO butler(b_id ,m_id, s_id,name) VALUES (96, 3, 52, 'bulter_one')")

# SELECT
# SELECT * FROM butler;
# SELECT name FROM butler;

# ORDER BY

# SELECT DISTINCT
# WHERE
# LIMIT
# BETWEEN
# IN
# LIKE
# IS NULL
# GLOB
# JOIN
# INNER JOIN
# LEFT JOIN
# CROSS JOIN
# SELF-JOIN
# FULL OUTER JOIN
# GROUP BY
# HAVING
# UNION
# EXECEPT
# INTERSECT
# SUBQUERY
# EXISTS
# CASE
# INSERT
# UPDATE
# DELETE
# REPLACE
# TRANSACTION


conn.commit()
conn.close()
