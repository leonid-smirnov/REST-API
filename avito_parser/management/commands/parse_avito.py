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
        p = int(input('Укажите страницу для парсинга: '))
        p = str(f'p={p}')
        print(p)

        # Ссылка на страницу для парсера
        url = 'https://www.avito.ru/kudrovo/kvartiry/prodam/vtorichka-ASgBAQICAUSSA8YQAUDmBxSMUg?' + p

        # Подключение к сайту через библиотеку Requests
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        # Парсим блок объявления
        announcement = soup.find_all('div', class_='iva-item-body-R_Q9c')

        # Проходим циклом по каждому элементу объявления и возвращаем нужные поля после парсинга

        for i in range(0, len(announcement)):
            # Парсим блок с заголовком
            title = announcement[i].findNext('h3', class_='title-root-j7cja iva-item-title-_qCwt '
                                                          'title-listRedesign-XHq38 title-root_maxHeight-SXHes '
                                                          'text-text-LurtD text-size-s-BxGpL text-bold-SinUO').text

            # Количество комнат
            room_number = announcement[i].findNext('h3', class_='title-root-j7cja iva-item-title-_qCwt '
                                                                'title-listRedesign-XHq38 title-root_maxHeight-SXHes '
                                                                'text-text-LurtD text-size-s-BxGpL text-bold-SinUO').text.strip(
                ',')
            # line.split(',')
            room_number = str(room_number[0: 15].replace(',', ''))

            # Площадь

            date = announcement[i].findNext('div', class_='date-text-VwmJG text-text-LurtD text-size-s-BxGpL '
                                                          'text-color-noaccent-P1Rfs').text

            # Парсим блок с ценой
            price = announcement[i].findNext('span',
                                             class_="price-text-E1Y7h text-text-LurtD text-size-s-BxGpL").text.strip(
                '₽').replace('\xa0', '')  # Убираем из цены пробелы и ненужные символы кодировки
            price = int(price)  # Переводим цену в числовой формат

            # Парсим блок с описанием
            description = announcement[i].findNext('div', class_='iva-item-text-_s_vh iva-item-description-S2pXQ '
                                                                 'text-text-LurtD text-size-s-BxGpL').text

            # Парсим блок со ссылкой на обьявление
            href = announcement[i].findNext('a', class_='link-link-MbQDP link-design-default-_nSbv title-root-j7cja '
                                                        'iva-item-title-_qCwt title-listRedesign-XHq38 '
                                                        'title-root_maxHeight-SXHes').attrs['href']

            url_a = 'www.avito.ru' + href  # коннектим url со ссылкой на объявление

            print(title)
            print(price)
            print(room_number)
            print(date)
            print(url_a)

            # Записываем полученнные данные из парсера в БД
            Product.objects.create(
                title=title,
                price=price,
                room_number=room_number,
                description=description,
                published_date=date,
                url=url_a,
            )


class Command(BaseCommand):
    help = 'Парсинг Авито'

    def handle(self, *args, **options):
        p = Parser()
        p.parse_block()
