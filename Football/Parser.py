import requests
import re
from lxml import html
import smtplib


def print_match():
    print(parsed_body.xpath('//title/text()')[0])  # title страницы
    index = 0
    index_t = 0
    while index < len(clubs):
        print(f"Дата: {date[index_t]}  Время: {time[index_t]}" if index_t < len(time) else f"Дата: {date[index_t]}", end='\n')
        print(f"{clubs[index]}  - : -  {clubs[index + 1]}")
        index += 2
        index_t += 1


response = requests.get('https://www.sports.ru/la-liga/calendar/')


"""
with open('test.html', 'w') as f:
    f.write(response.text)
"""

# Преобразование тела документа в дерево элементов (DOM)
parsed_body = html.fromstring(response.text)

clubs = parsed_body.xpath('//tbody//tr//td//a//@title')
date = re.findall("\d{2}\.\d{2}\.\d{4}", ' '.join(parsed_body.xpath('//tbody//tr//td//a//text()')))
time = re.findall("\d{2}:\d{2}", ' '.join(parsed_body.xpath('//tbody//tr//td//a//text()')))

print_match()

smtpObj = smtplib.SMTP('smtp..ru', 587)
smtpObj.starttls()
smtpObj.login('*****', '*******')
smtpObj.sendmail("*****", "****", "go to bed!")
smtpObj.quit()
