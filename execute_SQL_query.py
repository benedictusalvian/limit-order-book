from config import YOUR_DATABASE_HOST, YOUR_DATABASE_USER, YOUR_DATABASE_PASSWORD
import mysql.connector

def executeSQLquery(query):

    db = mysql.connector.connect(
        host = YOUR_DATABASE_HOST,
        user = YOUR_DATABASE_USER,
        password = YOUR_DATABASE_PASSWORD,
        database = 'order_book',
    )
    cursor = db.cursor()
    cursor.execute(query)
    data = []
    for item in cursor:
        data.append(item)
    print(data)
    return data