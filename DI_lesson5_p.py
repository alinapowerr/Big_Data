from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db = client['mail_ru_v5']
letters_link = db.letters_link

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.maximize_window()

driver.get('https://mail.ru/')

login = driver.find_element(By.CLASS_NAME, 'email-input')
login.send_keys('study.ai_172')
domain_name = driver.find_element(By.CLASS_NAME, 'domain-select')
select = Select(domain_name)
select.select_by_value('@mail.ru')
# login.send_keys(Keys.ENTER)
button = driver.find_element(By.CLASS_NAME, 'button')
button.click()
time.sleep(2)
password = driver.find_element(By.CLASS_NAME, 'password-input')
password.send_keys('NextPassword172#')
checkbox = driver.find_element(By.CLASS_NAME, 'saveauth')
checkbox.click()
second_button = driver.find_element(By.CLASS_NAME, 'second-button')
second_button.click()
time.sleep(5)

letters_set = set()
page = 0
while page < 3:
    letters = driver.find_elements(By.XPATH, "//div[contains(@class, 'dataset__items')]"
                                             "/a[contains(@class, 'js-letter-list-item')]")
    for letter in letters:
        link = letter.get_attribute('href')
        letters_set.add(link)
    actions = ActionChains(driver)
    actions.move_to_element(letters[-1])
    actions.perform()
    time.sleep(1)
    page += 1

for i in letters_set:
    letters_dict = {}
    driver.get(i)
    time.sleep(3)
    sender = driver.find_element(By.XPATH, "//div[@class='letter__author']/span[@class='letter-contact']").text
    date_send = driver.find_element(By.XPATH, "//div[@class='letter__author']/div[@class='letter__date']").text
    topic = driver.find_element(By.XPATH, "//div[@class='thread__subject-line']/h2").text
    letter_text = driver.find_element(By.XPATH, "//div[contains(@class, 'letter-body__body-content')]").text

    letters_dict['sender'] = sender
    letters_dict['date_send'] = date_send
    letters_dict['topic'] = topic
    letters_dict['letter_text'] = letter_text

    letters_link.insert_one(letters_dict)

# driver.close()

for doc in letters_link.find({}):
    print(doc)
result = letters_link.count_documents({})
print(result)
print()


# while driver.find_element_by_xpath("//a[contains(@class, 'list-letter-spinner_hidden')]"):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# SCROLL_PAUSE_TIME = 0.5
# last_height = driver.execute_script("return document.body.scrollHeight")
#
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(SCROLL_PAUSE_TIME)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

# letters[-1].getLocationOnScreenOnceScrolledIntoView()

