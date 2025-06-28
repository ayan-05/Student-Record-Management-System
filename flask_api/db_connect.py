import mysql.connector

def get_students():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='yourpassword',
        database='studentdb'
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
