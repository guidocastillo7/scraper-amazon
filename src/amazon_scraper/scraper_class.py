from bs4 import BeautifulSoup
from time import sleep

#Modelo para tomar los datos de los productos de la web
class AmazonScraper:

    #Se inicia con el driver de chrome
    def __init__(self, driver):
        self.driver = driver

    #Metodo que toma el html de la pagina con los productos listados
    def get_html(self, url):
        self.driver.get(url)
        sleep(5)

        content = self.driver.page_source
        html = BeautifulSoup(content, 'html.parser')

        self.driver.close()

        return html
    
    #Metodo que toma los datos especificos de cada producto (nombre, precio y url)
    def get_products(self, html_content):
        diccProductos = {}

        divProducto = html_content.find_all('div', {'class':'s-result-item'})

        for index, item in enumerate(divProducto):
            try:
                productoName = item.find('span', {'class':'a-size-base-plus a-color-base a-text-normal'}).text

                productoPrice = item.find('span', {'class':'a-price-whole'}).text.replace(',', ".") \
                    + item.find('span', {'class':'a-price-fraction'}).text
                
                productoUrl = item.find('a', {'class':'a-link-normal s-no-outline'}).attrs['href']

                diccProductos[str(index+1)] = [productoName, productoPrice, productoUrl]
            except Exception as e:
                pass

        return diccProductos
    
    #Metodo que toma el precio de un producto elegido de la bbdd mediante su url especifica
    def get_price(self, html_content: BeautifulSoup):
        new_price = html_content.find('span', {'class':'a-price-whole'}).text.replace(',', ".") \
            + html_content.find('span', {'class':'a-price-fraction'}).text
        
        return float(new_price)