import requests
import re
from lxml import html
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def look_match():
    index = 0
    index_t = 0
    with open('timetable.txt', 'w') as fp:
        fp.write(parsed_body.xpath('//title/text()')[0] + '\n')  # title страницы
        while index < len(clubs):
            fp.write(f"Дата: {date[index_t]}  Время: {time[index_t]} \n" if index_t < len(time) else f"Дата: {date[index_t]}\n")
            fp.write(f" {clubs[index]}  - : -  {clubs[index + 1]}\n")
            index += 2
            index_t += 1


def send_message(email_from, email_to):
    msg = MIMEMultipart()
    msg['Subject'] = "Footballs"
    with open('timetable.txt', 'r') as fp:
        msg = MIMEText(fp.read())

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login(email_from, '***')
    smtpObj.sendmail(email_from, email_to, msg.as_string())
    smtpObj.quit()


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

look_match()
#send_message("test.football.dima@gmail.com", "nagrdnk2017@mail.ru")



