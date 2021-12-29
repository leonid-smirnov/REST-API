import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from avito_parser.models import Product


class Parser:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
            'Accept-Language': 'ru',
        }

    @staticmethod
    def parse_block():
        # Ссылка на страницу для парсера
        url = 'https://www.avito.ru/kudrovo/kvartiry/prodam/vtorichka-ASgBAQICAUSSA8YQAUDmBxSMUg'

        # Подключение к сайту через библиотеку Requests
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        # Парсим блок объявления
        announcement = soup.find_all('div', class_='iva-item-body-R_Q9c')

        # '''Поля для парсинга'''
        #
        # # Парсим блок с заголовком
        # titles = soup.find_all('h3',
        #                        class_='title-root-j7cja iva-item-title-_qCwt title-listRedesign-XHq38 '
        #                               'title-root_maxHeight-SXHes text-text-LurtD text-size-s-BxGpL '
        #                               'text-bold-SinUO')
        #
        # # Парсим блок с ценой
        # price = soup.find_all('span', class_='price-text-E1Y7h text-text-LurtD text-size-s-BxGpL')
        #
        # # Парсим блок с описанием
        # description = soup.find_all('div', class_='iva-item-text-_s_vh iva-item-description-S2pXQ text-text-LurtD '
        #                                           'text-size-s-BxGpL')
        #
        # # Парсим блок со ссылкой
        # href = soup.find_all('a', class_='link-link-MbQDP link-design-default-_nSbv title-root-j7cja '
        #                                  'iva-item-title-_qCwt title-listRedesign-XHq38 title-root_maxHeight-SXHes')
        #
        # # Проходим циклом по каждому элементу объявления и возвращаем нужные поля после парсинга

        for i in range(0, len(announcement)):
            title = (announcement[i].findNext('h3', class_='title-root-j7cja iva-item-title-_qCwt '
                                                           'title-listRedesign-XHq38 title-root_maxHeight-SXHes '
                                                           'text-text-LurtD text-size-s-BxGpL text-bold-SinUO')).text

            price = (announcement[i].findNext('span', class_='price-text-E1Y7h text-text-LurtD text-size-s-BxGpL')).text

            description = (announcement[i].findNext('div', class_='iva-item-text-_s_vh iva-item-description-S2pXQ '
                                                                  'text-text-LurtD text-size-s-BxGpL')).text

            href = (announcement[i].findNext('a', class_='link-link-MbQDP link-design-default-_nSbv title-root-j7cja '
                                                         'iva-item-title-_qCwt title-listRedesign-XHq38 title-root_maxHeight-SXHes')).text

            print(title)  # Получаем текст заголовка без тегов

            print(price)  # Получаем цену без тегов
            print(description)
            print(href)

            # Product.objects.create(
            #     title=title,
            #     price=price,
            #     description=description,
            # #     url=url_a,
            # )


class Command(BaseCommand):
    help = 'Парсинг Авито'

    def handle(self, *args, **options):
        p = Parser()
        p.parse_block()
