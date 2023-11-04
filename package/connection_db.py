import sqlite3

def get_connection():
    connection = sqlite3.connect("D:\Git\ToDo-list\db\database.db")
    cursor = connection.cursor()

    return connection, cursor