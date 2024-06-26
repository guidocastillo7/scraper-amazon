import sqlite3

class GuardarProducto:

    def __init__(self):
        self.client = sqlite3.connect('amazon-scraper')

        self.db = self.client.cursor()

        self.db.execute('''
            CREATE TABLE IF NOT EXISTS producto (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price TEXT,
                url TEXT
            )
            ''')
        self.client.commit()


    def save_product(self, name: str, price: str, url: str):
        self.db.execute('''
            INSERT INTO producto (name, price, url)
            VALUES (?, ?, ?)
            ''', (name, price, url))
        
        self.client.commit()
        self.client.close()