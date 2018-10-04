from flask import Flask, render_template, request, jsonify
import sqlite3
app = Flask(__name__)

def get_todos():
    connection = sqlite3.connect('todoList.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todoList")
    todos = cursor.fetchall()
    connection.close()
    return todos

def insert_todo(post):
    connection = sqlite3.connect('todoList.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO todoList (todo) VALUES (?)",(post,))
    connection.commit()
    connection.close()

def delete_todo(id):
    connection = sqlite3.connect('todoList.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM todoList WHERE id =?",(id,))
    connection.commit()
    connection.close()

@app.route("/")
def index():
    posts = get_todos()
    print(posts)
    return render_template("index.html", posts=posts)


@app.route("/_post", methods=["POST"])
def post():
    todo = request.form['todo']
    insert_todo(todo)
    return jsonify({'post': todo, })

@app.route("/<string:id>/_delete", methods=["POST"])
def _delete(id):
    delete_todo(id)
    return jsonify({"message": "deleted"})



if __name__ == "__main__":
    app.run(port=5000, debug=True)
