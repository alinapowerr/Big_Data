from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import re
import json

main_url = 'https://naberezhnye.hh.ru/search/vacancy'
# page = 1
params = {'text': 'Junior python developer',
          'schedule': 'remote',
          # 'items_on_page': 50,
          'page': 0}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

vacancies_list = []
response = requests.get(main_url, params=params, headers=headers)

while response.ok:
    dom = bs(response.text, 'html.parser')
    results = dom.find('div', {'data-qa': 'vacancy-serp__results'})
    if not results:
        break
    vacancies = results.find_all('div', {'class': 'vacancy-serp-item'})

    for vacancy in vacancies:
        vacancy_data = {}
        info = vacancy.find('a', {'class': 'bloko-link', 'data-qa': 'vacancy-serp__vacancy-title'})
        name = info.text
        link = info.get('href')
        salary = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation',
                                       'class': 'bloko-header-section-3 bloko-header-section-3_lite'})
        if not salary:
            salary_rate = None
            salary_min = None
            salary_max = None
        else:
            salary_info_rate = salary.getText()
            salary_rate = re.sub("[^A-Za-z][^А-Яа-я]", "", salary_info_rate)
            # salary_rate = salary_info_rate[-1:-4]
            salary_sum = salary.getText().replace(u'\u202f', u'')
            salaries = salary_sum.split('–')
            salaries[0] = re.sub(r'[^0-9]', '', salaries[0])
            salary_min = int(salaries[0])
            if len(salaries) > 1:
                salaries[1] = re.sub(r'[^0-9]', '', salaries[1])
                salary_max = salaries[1]
            else:
                salary_max = None

        vacancy_data['name'] = name
        vacancy_data['link'] = link
        vacancy_data['salary_min'] = salary_min
        vacancy_data['salary_max'] = salary_max
        vacancy_data['salary_rate'] = salary_rate

        vacancies_list.append(vacancy_data)

    if not dom.find('a', {'data-qa': 'pager-next'}):
        break
    params['page'] += 1
    response = requests.get(main_url, params=params, headers=headers)

pprint(vacancies_list)

with open('hh_vacancies.json', 'w', encoding="utf-8") as f:
    for chunk in json.JSONEncoder(ensure_ascii=False,indent=4).iterencode(vacancies_list):
        f.write(chunk)
