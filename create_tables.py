import sqlite3

connection = sqlite3.connect('todoList.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS todoList (
id integer primary key,
todo text
)
""")

# insert values into the Todo List
cursor.execute("INSERT INTO todoLIST (todo) VALUES(?)",("Get Money",))
cursor.execute("INSERT INTO todoLIST (todo) VALUES(?)",("Go To Train",))
cursor.execute("INSERT INTO todoLIST (todo) VALUES(?)",("Workout",))
cursor.execute("INSERT INTO todoLIST (todo) VALUES(?)",("Meet Andrew",))
cursor.execute("INSERT INTO todoLIST (todo) VALUES(?)",("Code",))
cursor.execute("INSERT INTO todoLIST (todo) VALUES(?)",("Apply to Job",))

connection.commit()
connection.close()
