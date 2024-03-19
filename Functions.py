import psycopg2
conn = psycopg2.connect(host = "localhost", dbname="d", user="postgres", password ="141203", port = 5432 )

cur = conn.cursor()

def getAllStudents(conn):
  cur.execute("SELECT * FROM students;")
  for record in cur.fetchall():
    print(record)

def addStudent(conn, first_name, last_name, email, enrollment_date):
  cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);", (first_name, last_name, email, enrollment_date))
  conn.commit()

def updateStudentEmail(conn, student_id, new_email):
  cur.execute("UPDATE students SET email = %s WHERE student_id = %s;", (new_email, student_id))
  conn.commit()

def deleteStudent(conn,student_id):
  cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
  conn.commit()



# print("List of students:")
# getAllStudents(conn)

# print("\nAdd:")
# addStudent(conn, 'Sarah', 'Coash', 'sarah@example.com', '2024-09-06')
# getAllStudents(conn)

# print("\nUpdate:")
# updateStudentEmail(conn, 1, 'johnny@example.com')
# getAllStudents(conn)

print("\nDelete:")
deleteStudent(conn, 12)
getAllStudents(conn)
