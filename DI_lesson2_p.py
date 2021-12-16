from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

# 'https://naberezhnye.hh.ru/search/vacancy?text=Junior+python+developer&salary=&' \
#             'currency_code=RUR&experience=doesNotMatter&schedule=remote&order_by=relevance&search_period=0&' \
#             'items_on_page=50&no_magic=true&L_save_area=true'
main_url = 'https://naberezhnye.hh.ru/search/vacancy'
# page = 1
params = {'text': 'Junior python developer',
          'schedule': 'remote'}
          # 'page': page}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

response = requests.get(main_url, params=params, headers=headers)

if response.ok:
    dom = bs(response.text, 'html.parser')
    vacancies = dom.find_all('div', {'class': 'vacancy-serp-item',
                                          'data-qa': 'vacancy-serp__vacancy vacancy-serp__vacancy_standard_plus'})

    vacancies_list = []
    for vacancy in vacancies:
        vacancy_data = {}
        info = vacancy.find('a', {'class': 'bloko-link', 'data-qa': 'vacancy-serp__vacancy-title',
                                    'target': '_blank'})
        name = info.text
        link = info.get('href')
        # salary = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation', 'class': 'bloko-header-section-3 bloko-header-section-3_lite'}).text

        vacancy_data['name'] = name
        vacancy_data['link'] = link
        # vacancy_data['salary'] = salary

        vacancies_list.append(vacancy_data)

pprint(vacancies_list)