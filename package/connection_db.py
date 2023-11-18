import sqlite3
import os

def get_connection():
    try:
        connection = sqlite3.connect("db\database.db")
        
    except:
        os.mkdir("db")
        connection = sqlite3.connect("db\database.db")
        
    cursor = connection.cursor()

    return connection, cursor