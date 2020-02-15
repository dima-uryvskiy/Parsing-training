import requests
from lxml import html
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def write_in_file(title, clubs, time, score, tour):
    index, index_s = 0, 0
    with open('timetable.txt', 'w') as fp:
        fp.write(title[0] + '\n')
        while index < len(clubs):
            if index % 20 == 0:
                fp.write('\t' + tour[index // 20] + '\n')
            fp.write(f"Дата: {time[index]}  Время: {time[index + 1]} \n")
            fp.write(f"\t\t{clubs[index]} {score[index_s]} {clubs[index + 1]} \n")
            index += 2
            index_s += 1


def parsing():
    response = requests.get('https://www.sports.ru/epl/calendar/')
    parsed_body = html.fromstring(response.text)
    title = parsed_body.xpath('//title/text()')
    time = [value.strip() for value in parsed_body.xpath("//td[@class=\"name-td alLeft\"]/span/text() | //td[@class=\"name-td alLeft\"]/a/text()")]
    if "перенесен" in time:
        time.insert(time.index("перенесен") + 1, '-')
    clubs = parsed_body.xpath("//tbody/tr/td//a[@class=\"player\"]/text()")
    score = parsed_body.xpath("//td[@class=\"score-td\"]/a[@class=\"score\"]/noindex/b/text()")
    tour = parsed_body.xpath('(//h3)/text()')
    print(tour)
    write_in_file(title, clubs, time, score, tour)


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






parsing()
#send_message("test.football.dima@gmail.com", "nagrdnk2017@mail.ru")



