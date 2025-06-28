from flask import Flask, jsonify
from db_connect import get_students

app = Flask(__name__)

@app.route('/students')
def get_all_students():
    students = get_students()
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)
