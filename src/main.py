from amazon_scraper.scraper_class import AmazonScraper
from amazon_scraper.producto_bbdd import GuardarProducto
from selenium import webdriver


def init():

    #Iniciamos dando dos opciones al usuario para elegir
    print('Que operacion quieres hacer? \n1: Buscar nuevo producto y guardarlo en bbdd. \
          \n2: Revisar precio actual de un producto ya guardado.')
    ope = input('Ingresa la operacion deseada: ')

    #Opcion que busca el producto escrito por el usuario y guarda en la bbdd el elegido
    if ope == '1':
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

        eleccion = input('Ingresa el id del producto deseado: ')
        db_name = products_result[eleccion][0]
        db_price = products_result[eleccion][1]
        db_url = 'https://www.amazon.it' + products_result[eleccion][2]

        bbdd = GuardarProducto()
        bbdd.save_product(
            name=db_name,
            price=db_price,
            url=db_url
        )

    #Opcion que revisa el precio en pagina actual de un producto elegido de la bbdd
    #Y lo compara con el precio guardado en la bbdd
    elif ope == '2':
        bbdd = GuardarProducto()
        bbdd.read_product()
        bbdd.check_product()

    else:
        print('Opcion invalida!')

    

if __name__ == '__main__':
    init()