import psycopg2
connection = psycopg2.connect(
host='localhost',
database='trip',
user='test1',
password='test1'
)


def get_tourist():
	cursor = connection.cursor()
	cursor.execute("select * from tourist")
	rows = cursor.fetchall()
	cursor.close()
	return rows

def add_tourist(id,name,phone_no):
  cursor = connection.cursor()
  cursor.execute(f"""insert into tourist
                 values ({id},'{name}',{phone_no})""")
  connection.commit()
  cursor.close()