import requests

from bs4 import BeautifulSoup

import sqlite3

from datetime import datetime


# підключаємося до бази даних

conn = sqlite3.connect('weather.db')

c = conn.cursor()


# створюємо таблицю

c.execute('''CREATE TABLE IF NOT EXISTS weather

            (date_time text, temperature real)''')


# отримуємо дані з сайту погоди

url = 'https://www.meteoprog.ua/ua/weather/Kyiv/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

temperature = soup.find('span', class_='temp').get_text()


# записуємо дані до бази даних

now = datetime.now()

date_time = now.strftime("%Y-%m-%d %H:%M:%S")

c.execute("INSERT INTO weather (date_time, temperature) VALUES (?, ?)", (date_time, temperature))

conn.commit()


# закриваємо з'єднання з базою даних

conn.close()
