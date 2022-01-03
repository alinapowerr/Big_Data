# Написать приложение, которое собирает основные новости с сайта на выбор news.mail.ru, lenta.ru, yandex-новости.
# Для парсинга использовать XPath. Структура данных должна содержать:
# название источника;
# наименование новости;
# ссылку на новость;
# дата публикации.
# Сложить собранные новости в БД

import requests
from lxml import html
from pprint import pprint
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError as dke

client = MongoClient('127.0.0.1', 27017)
db = client['news_2022']
lenta_ru = db.lenta_ru
lenta_ru.create_index([('link', 1)], unique=True)

url = 'https://lenta.ru'
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

response = requests.get(url, headers=header)
dom = html.fromstring(response.text)

items = dom.xpath("//a[contains(@class, '_topnews')]")

for item in items:
    news_data = {}
    name = item.xpath("./div[contains(@class, 'mini__text')]/span[contains(@class, 'mini__title')]/text()"
                      "|./div[contains(@class, 'big__titles')]/h3/text()")[0]
    link = item.xpath("./@href")[0]
    if link.startswith('https'):
        source = link
    else:
        source = url

    if link.startswith('/news/202', 0, 9):
        response2 = requests.get(url + link, headers=header)
        dom2 = html.fromstring(response2.text)
        date = dom2.xpath("//time[contains(@class, 'topic-header__time')]/text()")
    else:
        date = item.xpath(".//time[contains(@class, '__date')]/text()")

    news_data['name'] = name
    news_data['link'] = link
    news_data['source'] = source
    news_data['publication_date'] = date

    try:
        lenta_ru.insert_one(news_data)
    except dke:
        print(f"Документ с id={lenta_ru['_id']} уже существует")


for doc in lenta_ru.find({}):
    pprint(doc)

result = lenta_ru.count_documents({})
print(result)

