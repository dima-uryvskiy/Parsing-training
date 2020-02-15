import requests
from lxml import html
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def main_menu():
    urls_calendar = {1: 'epl', 2: 'la-liga', 3: 'seria-a',  4: 'bundesliga', 5: 'ligue-1'}
    print("Select league:\n"
          "1 - Premier League(English)\n"
          "2 - LaLiga(Spanish)\n"
          "3 - Serie A(Italy)\n"
          "4 - Bundesliga(Germany)\n"
          "5 - Ligue 1(France)\n"
          "Enter number: ", end='')
    # по хорошему нужно смотреть что вводит пользователь но это потом
    return f"https://www.sports.ru/{urls_calendar[int(input())]}/calendar"


def write_in_file(title, clubs, time, score, tour):
    index, index_s = 0, 0
    with open('timetable.txt', 'w') as fp:
        fp.write(title[0] + '\n')  # заголовок файла
        while index < len(clubs):
            if index % 20 == 0:  # записываю какой тур (примерно в туре 10 матчей тк 2 команды то 20)
                fp.write('\n\t\t\t' + tour[index // 20] + '\n\n')
            fp.write(f"Дата: {time[index]}  Время: {time[index + 1]} \n")  # запись основной информации
            fp.write(f"\t{clubs[index]} {score[index_s]} {clubs[index + 1]} \n")
            index += 2
            index_s += 1


def parsing(url):
    response = requests.get(url)
    parsed_body = html.fromstring(response.text)
    title = parsed_body.xpath('//title/text()')  # получаю заголовок
    time = [value.strip() for value in parsed_body.xpath("//td[@class=\"name-td alLeft\"]/span/text() | "
                                                         "//td[@class=\"name-td alLeft\"]/a/text()")]  # получаю дату
    if "перенесен" in time:  # если вдруг матч перенесен необходимо отлавливать это
        time.insert(time.index("перенесен") + 1, '-')
    clubs = parsed_body.xpath("//tbody/tr/td//a[@class=\"player\"]/text()")  # получаю клубы
    score = parsed_body.xpath("//td[@class=\"score-td\"]/a[@class=\"score\"]/noindex/b/text()")  # получаю счет
    tour = parsed_body.xpath('(//h3)/text()')  # получаю туры
    write_in_file(title, clubs, time, score, tour)


def send_message(email_from, email_to):
    msg = MIMEMultipart()
    msg['Subject'] = "Footballs"
    with open('timetable.txt', 'r') as fp:  # данные из файла для отправки
        msg = MIMEText(fp.read())

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login(email_from, 'password')
    smtpObj.sendmail(email_from, email_to, msg.as_string())
    smtpObj.quit()


parsing(main_menu())  # передаю utl полученный при выборе пользователя
send_message("test.football.dima@gmail.com", "test_email")



