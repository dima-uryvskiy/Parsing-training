import csv
import requests
from bs4 import BeautifulSoup
import re


def get_html(url):
    response = requests.get(url)
    return response.text


def get_count_pages(html):
    soup = BeautifulSoup(html, "lxml")
    pages = soup.find("div", class_="pagination-pages clearfix").find_all("a", class_="pagination-page")[-1].get("href")
    return int(re.search("[\d]+", pages).group())   # количество страниц


def get_page_data(html):
    soup = BeautifulSoup(html, "lxml")
    info_product = soup.find("div", class_="js-catalog_serp").find_all_next("div", class_="item__line")
    write_in_file(info_product)


def parsed_info(data, tag, class_tag):
    try:
        result = data.find(tag, class_=class_tag).text.strip()
    except AttributeError:
        result = ""
    return result


def write_in_file(info):
    with open(f"./products/info_product_page_{num}.csv", "w") as file:
        for data in info:
            name = parsed_info(data, "a", "snippet-link")
            price = parsed_info(data, "div", "snippet-price-row")
            address = parsed_info(data, "span", "item-address-georeferences-item__content")
            time_published = parsed_info(data, "div", "snippet-date-info")
            try:
                link = "https://www.avito.ru" + data.find("a", class_="snippet-link").get("href")
            except AttributeError:
                link = ""
            file.write(f"{name},{price},{address},{time_published},{link}\n")


def print_info(num_page):
    with open(f"./products/info_product_page_{num_page}.csv", newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for row in reader:
            print(', '.join(row))


start_url = "https://www.avito.ru/moskva/telefony?q=Iphone"
for num in range(1, get_count_pages(get_html(start_url)) + 1):
    url_gen = start_url + f"&p={num}"
    get_page_data(get_html(url_gen))




