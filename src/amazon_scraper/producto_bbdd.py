import sqlite3

class GuardarProducto:

    def __init__(self):
        self.client = sqlite3.connect('amazon-scraper')

        self.db = self.client.cursor()


    def save_product(self, name: str, price: str, url: str, ):
        self.db.execute('''
            INSERT INTO product (name, price, url)
            VALUES (?, ?, ?, ?, ?)
            ''', (name, price, url))
        
        self.client.commit()