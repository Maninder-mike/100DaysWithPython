import psycopg2

# add database with python code
conn = psycopg2.connect("dbname=office user=postgres password=123456")

cur = conn.cursor()

# cur.execute("INSERT INTO head_office(name, employees) VALUES('PUNJAB PVT. LTD.', 31)")

# cur.execute(
#     """INSERT INTO head_office(name, employees) VALUES
# 	('KUWAIT PVT. LTD.', 5),
# 	('CANADA PVT. LTD.', 21),
# 	('USA PVT. LTD.', 15),
# 	('ENGLAND PVT. LTD.', 25)
# """
# )

cur.execute(
    """INSERT INTO sub_office(name, employees) VALUES
	('patran', 5),
	('calgary', 21),
	('adminton', 15),
	('california', 25)
"""
)

conn.commit()
conn.close()
