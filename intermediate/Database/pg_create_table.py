from psycopg2 import connect

# add database with python code
conn = psycopg2.connect("dbname=office user=postgres password=123456")

cur = conn.cursor()

cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')

# create a table, if table exists than this line skips
cur.execute(
    """CREATE TABLE IF NOT EXISTS head_office(
	name TEXT NOT NULL UNIQUE,
	employees smallint NOT NULL,
	ho_id uuid NOT NULL DEFAULT uuid_generate_v4(),
	add_date DATE NOT NULL default CURRENT_DATE,
	PRIMARY KEY(ho_id)
)"""
)

cur.execute(
    """CREATE TABLE IF NOT EXISTS sub_office(
	name TEXT NOT NULL UNIQUE,
	employees smallint NOT NULL,
	head_office uuid,
	so_id INT GENERATED ALWAYS AS IDENTITY,
	add_datetime DATE NOT NULL default now(),
	PRIMARY KEY(so_id), 
	CONSTRAINT fk_ho FOREIGN KEY(head_office) REFERENCES head_office(ho_id)
)"""
)

conn.commit()
conn.close()
