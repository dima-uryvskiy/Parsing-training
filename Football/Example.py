import requests
import re
from lxml import html
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




def look_match():
    response = requests.get('https://www.sports.ru/la-liga/calendar/')
    parsed_body = html.fromstring(response.text)

    time = parsed_body.xpath("//tbody/tr/td[@class=\"name-td alLeft\"]/a/text()")
    owner_clubs = parsed_body.xpath("(//tbody/tr/td[@class=\"owner-td\"]//a[@class=\"player\"]/text())")
    guests_clubs = parsed_body.xpath("(//tbody/tr/td[@class=\"guests-td\"]//a[@class=\"player\"]/text())")
    print(len(time))
    print(len(owner_clubs))
    index = 0
    with open('timetable.txt', 'w') as fp:
        fp.write(parsed_body.xpath('//title/text()')[0] + '\n')  # title страницы
        while index < len(owner_clubs):
            fp.write(parsed_body.xpath('(//h3)[1]/text()')[0] + '\n')
            fp.write(f"Дата: {time[index]}  Время: {time[index  + 1]}" + " \n")
            fp.write(f"{owner_clubs[index]} : {guests_clubs[index]}" + " \n")
            index += 1



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


look_match()
#send_message("test.football.dima@gmail.com", "nagrdnk2017@mail.ru")



