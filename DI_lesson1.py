"""
1. Посмотреть документацию к API GitHub,
разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.
"""

import requests
import json

# user = input('Enter the username: ')
# url = 'https://api.github.com/users/'+user+'/repos'
#
# response = requests.get(url)
# # print(response.json())
# repositories_list = []
#
# if response.ok:
#     for i in response.json():
#         repositories_list.append(i['name'])
#     print(f'List of user repositories {user}: ')
#     print(repositories_list)
#
# with open('user_repos.json', 'w') as f:
#     json.dump(repositories_list, f)


"""
2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа). 
Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл. 
"""

" 2.1. OpenWeather | Information about the weather in any city "

# api_url = 'http://api.openweathermap.org/data/2.5/weather'
# api_key = input("Enter your APPID: ")
# city = input("Enter the name of the city: ")
#
# response = requests.get(url=api_url, params={'q': city, 'units': 'metric', 'lang': 'eng', 'APPID': api_key})
# data = response.json()
# # print(data)
# print(f"Now in {city}:", data['weather'][0]['description'])
# print("Temperature:", data['main']['temp'])
#
# with open('data_weather.json', 'w') as f:
#     json.dump(data, f)

" 2.2. NASA | Astronomy Picture of the Day "

# api_url = 'https://api.nasa.gov/planetary/apod'
# api_key = 'DEMO_KEY'
# user_date = input('Enter a date to see astronomy picture of the day. '
#                   'Date must be between Jun 16, 1995 and Dec 12, 2021. '
#                   'i.e. 2017-07-01: ')
# response = requests.get(url=api_url, params={'date': user_date, 'api_key': api_key})
# data = response.json()
# # print(data)
# print('Click this link to see astronomy picture of the day -->', data['hdurl'])
# print('Explanation: ', data['explanation'])


" 2.3 NASA | Mars Weather Service API "

# api_url = 'https://api.nasa.gov/insight_weather/?'
# api_key = 'DEMO_KEY'
#
# response = requests.get(url=api_url, params={'api_key': api_key, 'feedtype': 'json', 'ver': '1.0'})
# data = response.json()
# # print(data)
# print('For the current date', data['1081']['Last_UTC'],
#       'on Mars', data['1081']['AT']['av'], '°F.',
#       'Horizontal wind speed sensor summary data is', data['1081']['HWS']['av'], 'm/s')





