import sqlite3

def get_connection():
    connection = sqlite3.connect("../db/database.db")
    cursor = connection.cursor()

    return connection, cursor