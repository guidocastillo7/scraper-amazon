import sqlite3
from .scraper_class import AmazonScraper
from selenium import webdriver

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


    def read_product(self):
        self.db.execute("SELECT * from producto")
        productos = self.db.fetchall()

        for i in productos:
            print(f'{i[0]}.- {i[1]}: €{i[2]}', end='\n\n')


    def check_product(self):
        check = input('Ingresa el id del producto que quieres revisar: ')
        self.db.execute("SELECT * FROM producto WHERE id = ?", (check,))

        resultado = self.db.fetchone()
        price_bbdd = resultado[2]
        print(f'Precio en bbdd: {price_bbdd}')

        option = webdriver.ChromeOptions()
        option.binary_location = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

        scraper = AmazonScraper(driver= webdriver.Chrome(options= option))
        html_check = scraper.get_html(resultado[3])
        price_check = scraper.get_price(html_content= html_check)
        print(f'Precio actual: {price_check}')

        if price_check > float(price_bbdd):
            print('El producto aumento de precio')

        elif price_check < float(price_bbdd):
            print('El producto bajo de precio')

        elif price_check == float(price_bbdd):
            print('El producto no ha cambiado precio')