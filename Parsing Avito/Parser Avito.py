import requests
from bs4 import BeautifulSoup

start_url = "https://www.avito.ru/moskva/telefony?q=Iphone"


def get_html(url):
    response = requests.get(url)
    return response.text


def get_count_pages(html):
    soup = BeautifulSoup(html, "lxml")
    pages = soup.find("div", class_="pagination-pages clearfix").find_all("a", class_="pagination-page")
    print(*pages, sep='\n')


get_count_pages(get_html(start_url))