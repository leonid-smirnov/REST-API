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
        url = 'https://www.avito.ru/kudrovo/kvartiry/prodam/vtorichka-ASgBAQICAUSSA8YQAUDmBxSMUg'  # Ссылка на
                                                                                                   # страницу для парсера
        response = requests.get(url)  # Подключение к сайту через библиотеку Requests
        soup = BeautifulSoup(response.text, 'lxml')

        '''Поля для парсинга'''

        titles = soup.find_all('h3', class_='title-root-j7cja iva-item-title-_qCwt title-listRedesign-XHq38 '
                                            'title-root_maxHeight-SXHes text-text-LurtD text-size-s-BxGpL '
                                            'text-bold-SinUO')  # Парсим блок с заголовком
        price = soup.find_all('meta', attrs={'itemprop': 'price'})  # Парсим блок с ценой

        description = soup.find_all('meta', attrs={'itemprop': 'description'})  # Парсим блок с описанием

        href = soup.find_all('a', 'link-link-MbQDP link-design-default-_nSbv title-root-j7cja iva-item-title-_qCwt '
                                  'title-listRedesign-XHq38 title-root_maxHeight-SXHes')  #  Парсим ссылку на объявление

        for i in range(0, len(titles)):
            print(titles[i].text)  # Получаем текст заголовка без тегов
            price[i] = (price[i].attrs['content'])  # Получаем цену без тегов
            description[i] = (description[i].attrs['content'])  # Получаем описание без тегов
            int(price[i])
            print(price[i])
            print(description[i])
            href[i] = (href[i].attrs['href'])

            a = 'https://www.avito.ru'
            url_a = (a + (href[i]))
            print(url_a)

            Product.objects.create(
                title=titles[i].text,
                price=price[i],
                description=description[i],
                url=url_a,
            )


class Command(BaseCommand):
    help = 'Парсинг Авито'

    def handle(self, *args, **options):
        p = Parser()
        p.parse_block()


import datetime
import urllib.parse
# from collections import namedtuple
from logging import getLogger

import bs4
# import requests
from django.core.management.base import BaseCommand, CommandError

# from avito_parser.models import Product
#
# logger = getLogger(__name__)
#
# # InnerBlock = namedtuple('Block', 'title,price,currency,date,url')
# #
# #
# # class Block(InnerBlock):
# #     def __str__(self):
# #         return f'{self.title}\t{self.price}\t{self.currency}\t{self.date}\t{self.url}'
#
#
# class AvitoParser:
#
# def __init__(self):
#     self.session = requests.Session()
#     self.session.headers = {
#         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
#         'Accept-Language': 'ru',
#     }

#     def get_page(self, page: int = None):
#         params = {
#             'radius': 0,
#             'cd': 1,
#         }
#         if page and page > 1:
#             params['p'] = page
#         url = 'https://www.avito.ru/kudrovo/avtomobili/s_probegom/'
#         r = self.session.get(url, params=params)
#         return r.text
#
#     @staticmethod
#     def parse_date(item: str):
#         params = item.strip().split(' ')
#         # print params
#         if len(params) == 2:
#             day, time = params
#             if day == 'Сегодня':
#                 date = datetime.date.today()
#             elif day == 'Вчера':
#                 date = datetime.date.today() - datetime.timedelta(days=1)
#             else:
#                 print('Не смогли разобрать день', item)
#                 return
#
#             time = datetime.datetime.strptime(time, '%H:%M').time()
#             return datetime.datetime.combine(date=date, time=time)
#
#         elif len(params) == 3:
#             day, month_hru, time = params
#             day = int(day)
#             month_map = {
#                 'января': 1,
#                 'февраля': 2,
#                 'марта': 3,
#                 'апреля': 4,
#                 'мая': 5,
#                 'июня': 6,
#                 'июля': 7,
#                 'августа': 8,
#                 'сентября': 9,
#                 'октября': 10,
#                 'ноября': 11,
#                 'декабря': 12,
#             }
#             month = month_map.get(month_hru)
#             if not month:
#                 print('Не смогли разобрать месяц:', item)
#                 return
#
#             today = datetime.datetime.today()
#             time = datetime.datetime.strptime(time, '%H:%M')
#             return datetime.datetime(day=day, month=month, year=today.year, hour=time.hour)
#
#         else:
#             print('Не смогли разобрать формат', item)
#             return
#
#     def parse_block(self, item):
#         #  Блок со ссылкой
#         url_block = item.select_one('a.link-link-MbQDP link-design-default-_nSbv title-root-j7cja iva-item-title-_qCwt title-listRedesign-XHq38 title-root_maxHeight-SXHes')
#         if not url_block:
#             raise CommandError('bad "url_block" css')
#
#         href = url_block.get('href')
#         if href:
#             url = 'https://www.avito.ru' + href
#         else:
#             url = None
#
#         #  Выбрать блок с названием
#         title_block = item.select_one('a.link-link-MbQDP link-design-default-_nSbv title-root-j7cja iva-item-title-_qCwt title-listRedesign-XHq38 title-root_maxHeight-SXHes')
#         if not title_block:
#             raise CommandError('bad "title_block" css')
#         title = title_block.string.strip()
#         logger.info('title: %s', title)
#
#         # #  Выбрать блок с названием и валютой
#         price_block = item.select_one('a.link-link-MbQDP link-design-default-_nSbv title-root-j7cja iva-item-title-_qCwt title-listRedesign-XHq38 title-root_maxHeight-SXHes')
#         if not price_block:
#             raise CommandError('bad "price_block" css')
#
#         price_block = price_block.get_text('\n')
#         price_block = list(filter(None, map(lambda i: i.strip(), price_block.split('\n'))))
#         if len(price_block) == 2:
#             price, currency = price_block
#             price = int(price.replace(' ', ''))
#         elif len(price_block) == 1:
#             #  Бесплатно
#             price, currency = 0, None
#         else:
#             price, currency = None, None
#             print(f'Что-то не так при поиске цены: {price_block}, {url}')
#
#         # #  Выбрать блок с датой размещения объявления
#         date = None
#         date_block = item.select_one('a.link-link-MbQDP link-design-default-_nSbv title-root-j7cja iva-item-title-_qCwt title-listRedesign-XHq38 title-root_maxHeight-SXHes')
#         if not date_block:
#             raise CommandError('bad "date_block" css')
#
#         absolute_date = date_block.get('item-date')
#         if absolute_date:
#             date = self.parse_date(item=absolute_date)
#
#         # bbb = Product(
#         #     title=title,
#         #     price=price,
#         #     currency=currency,
#         #     url=url,
#         #     date=date,
#         # ).save()
#         # print(bbb)
#
#         try:
#             p = Product.objects.get(url=url)
#             p.title = title
#             p.price = price
#             p.currency = currency
#             p.save()
#         except Product.DoesNotExist:
#             p = Product(
#                 url=url,
#                 title=title,
#                 price=price,
#                 currency=currency,
#                 published_date=date,
#             ).save()
#
#         logger.debug(f'product {p}')
#
#
#     def get_pagination_limit(self):
#         text = self.get_page()
#         soup = bs4.BeautifulSoup(text, 'lxml')
#         print(soup.prettify())
#
#         container = soup.select('a.pagination-page')
#         if not container:
#             return 1
#         last_button = container[-1]
#         href = last_button.get('href')
#         if not href:
#             return 1
#
#         r = urllib.parse.urlparse(href)
#         params = urllib.parse.parse_qs(r.query)
#         return int(params['p'][0])
#
#     def get_blocks(self, page: int = None):
#         text = self.get_page(page=page)
#         soup = bs4.BeautifulSoup(text, 'lxml')
#
#         #  Запрос из css селектора из множества классов, производится через селект
#         container = soup.select('a.link-link-MbQDP link-design-default-_nSbv title-root-j7cja iva-item-title-_qCwt title-listRedesign-XHq38 title-root_maxHeight-SXHes')
#         for item in container:
#             self.parse_block(item=item)
#
#     def parse_all(self):
#         limit = self.get_pagination_limit()
#         print(f'Всего страниц: {limit}')
#
#         for i in range(1, limit + 1):
#             self.get_blocks(page=i)
#
#
# class Command(BaseCommand):
#     help = 'Парсинг Авито'
#
#     def handle(self, *args, **options):
#         p = AvitoParser()
#         p.parse_all()
