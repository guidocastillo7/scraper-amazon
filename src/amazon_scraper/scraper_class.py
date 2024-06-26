from bs4 import BeautifulSoup
from time import sleep

class AmazonScraper:

    def __init__(self, driver):
        self.driver = driver


    def get_html(self, url):
        self.driver.get(url)
        sleep(5)

        content = self.driver.page_source
        html = BeautifulSoup(content, 'html.parser')

        self.driver.close()

        return html
    

    def get_products(self, html_content):
        diccProductos = {}

        divProducto = html_content.find_all('div', {'class':'s-result-item'})

        for index, item in enumerate(divProducto):
            try:
                productoName = item.find('span', {'class':'a-size-base-plus a-color-base a-text-normal'}).text

                productoPrice = item.find('span', {'class':'a-price-whole'}).text \
                    + item.find('span', {'class':'a-price-fraction'}).text
                
                productoUrl = item.find('a', {'class':'a-link-normal s-no-outline'}).attrs['href']

                diccProductos[str(index+1)] = [productoName, productoPrice, productoUrl]
            except Exception as e:
                pass

        return diccProductos