import os
import psycopg2

class DBConnection:
    
    DATABASE_URL = os.environ.get("DATABASE_URL")

    def __init__(self):
        conn = psycopg2.connect(self.DATABASE_URL)
        conn.autocommit = True
        self.cursor = conn.cursor()
        self.cursor.execute(open('tables.sql', 'r').read())
        print(self.cursor)