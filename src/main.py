from amazon_scraper.scraper_class import AmazonScraper
from selenium import webdriver


def init():
    item = input('Ingrese el nombre del producto: ')

    option = webdriver.ChromeOptions()
    option.binary_location = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

    search_url = 'https://www.amazon.it/s?k={}'.format(item)

    amazonScraper = AmazonScraper(driver= webdriver.Chrome(options= option))
    result_html = amazonScraper.get_html(search_url)

    products_result = amazonScraper.get_products(html_content= result_html)

    contador = 0
    for clave, valor in products_result.items():
        contador += 1
        print(f'{clave}.- {valor[0]}: €{valor[1]}', end='\n\n')

        if contador == 5:
            break

if __name__ == '__main__':
    init()