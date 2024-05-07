import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS producao (
                id INTEGER PRIMARY KEY,
                produto TEXT,
                quantidade INTEGER,
                ano INTEGER
            )
        ''')
        conn.commit()
        conn.close()

    def insert_data(self, data):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.executemany('''
            INSERT INTO producao (id, produto, quantidade, ano)
            VALUES (?, ?, ?, ?)
        ''', data)
        conn.commit()
        conn.close()
