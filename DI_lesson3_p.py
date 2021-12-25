from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import re
import json
import pymongo
from pymongo import MongoClient
from pprint import pprint
from pymongo.errors import DuplicateKeyError as dke
import hashlib

"1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB " \
"и реализовать функцию, которая будет добавлять только новые вакансии/продукты в вашу базу."

client = MongoClient('127.0.0.1', 27017)
db = client['hh_vacancies']
vacancy_python = db.vacancy_python
vacancy_python.create_index([('link', 1)], unique=True)

main_url = 'https://naberezhnye.hh.ru/search/vacancy'
params = {'text': 'Junior python developer',
          'schedule': 'remote',
          'page': 0}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
response = requests.get(main_url, params=params, headers=headers)

# while response.ok:
#     dom = bs(response.text, 'html.parser')
#     results = dom.find('div', {'data-qa': 'vacancy-serp__results'})
#     if not results:
#         break
#     vacancies = results.find_all('div', {'class': 'vacancy-serp-item'})
#
#     for vacancy in vacancies:
#         vacancy_data = {}
#         info = vacancy.find('a', {'class': 'bloko-link', 'data-qa': 'vacancy-serp__vacancy-title'})
#         name = info.text
#         link = info.get('href')
#         salary = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation',
#                                        'class': 'bloko-header-section-3 bloko-header-section-3_lite'})
#         if not salary:
#             salary_rate = None
#             salary_min = None
#             salary_max = None
#         else:
#             salary_info = salary.getText().replace(u'\u202f', u'')
#             salaries = re.split(r'\s+', re.sub(r'–', ' ', salary_info).strip())
#             if salaries[0].isdigit():
#                 salary_min = int(salaries[0])
#             elif salaries[0] == 'от':
#                 salary_min = int(salaries[1])
#             else:
#                 salary_min = None
#             if len(salaries) > 1 and salaries[0].isdigit():
#                 salary_max = int(salaries[1])
#             elif salaries[0] == 'до':
#                 salary_max = int(salaries[1])
#             else:
#                 salary_max = None
#             salary_info_rate = salary.getText()
#             salary_rate = salaries[-1]
#
#         vacancy_data['name'] = name
#         vacancy_data['link'] = link
#         vacancy_data['salary_min'] = salary_min
#         vacancy_data['salary_max'] = salary_max
#         vacancy_data['salary_rate'] = salary_rate
#
#         try:
#             vacancy_python.insert_one(vacancy_data)
#         except dke:
#             print(f"Документ с id={vacancy_data['_id']} уже существует")
#
#     if not dom.find('a', {'data-qa': 'pager-next'}):
#         break
#     params['page'] += 1
#     response = requests.get(main_url, params=params, headers=headers)

for doc in vacancy_python.find({}):
    pprint(doc)

result = vacancy_python.count_documents({})
print(result)


"2. Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой " \
"больше введённой суммы (необходимо анализировать оба поля зарплаты)."

a = int(input('Введите сумму заработной платы: '))

for doc in vacancy_python.find({'$and': [{'salary_min': {'$gte': a}},
                                  {'salary_max': {'$gte': a}}
                                 ]}):
    pprint(doc)




# mongoimport -d hh -c vacancy_python /Users/alina/PycharmProjects/GB/data_internet/2.\ Parsing\ HTML.\ BeautifulSoup\,\ MongoDB/hh_vacancies.json
