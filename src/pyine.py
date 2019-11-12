from requests_html import HTMLSession
from pprint import pprint
from re import search


def main():
    session = HTMLSession()
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
    }
    url = 'http://www.ine.gub.uy/web/guest/cotizacion-de-monedas2'
    url = 'http://www.ine.gub.uy/web/guest/ipc-indice-de-precios-al-consumo'
    url = 'http://www.ine.gub.uy/web/guest/ims-indice-medio-de-salarios'
    response = session.get(url, headers=header)
    response.html.render(sleep=.5)

    print(response.html.html)

    link_cotizacion = search('<a href="(http://www\.ine\.gub\.uy/c.+?groupId.+?)"> Cotización monedas<span', response.html.html)[1]
    pprint('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    pprint(link_cotizacion)

    excel_cotizacion = session.get(link_cotizacion, headers=header)
    pprint(excel_cotizacion.html.html)
    # open('Cotizaciones.xlsx', mode='wb').write(excel)


if __name__ == "__main__":
    main()
