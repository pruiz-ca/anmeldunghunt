#!/usr/bin/env python3
from datetime import datetime, timedelta, date
from bs4 import BeautifulSoup as bs
from time import sleep
import webbrowser
import requests
import os


url = ''  # URL of the website with the calendar of the appointments
# Range for dates to check
deadline = datetime(2022, 12, 31)
tomorrow = datetime.combine(
    date.today() + timedelta(days=1), datetime.min.time())

session = requests.Session()

while True:
    try:
        res = session.get(url)
        if (res.status_code != 200):
            raise Exception('Web page loading failed')
        html = bs(res.content, 'html.parser')

        bookings = html.find_all('td', {'class': 'buchbar'})
        links = [booking.find('a') for booking in bookings]

        for link in links:
            date = datetime.fromtimestamp(int(link['href'].split('/')[-2]))
            date_str = date.strftime('%Y-%m-%d')
            if (date >= tomorrow and date <= deadline):
                webbrowser.open_new("https://service.berlin.de" + link['href'])
                print(f':) found appointment at {date}')
                os.system('say "Termin found"')
        sleep(10)

    except Exception as e:
        os.system('say Error; sleep 1; say Error; sleep 1; say Error')
        print(f'Error: {e}')
