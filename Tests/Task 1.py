import requests
import re
from lxml import html

response = requests.get('https://www.google.com/search?q=xpath')
parsed_body = html.fromstring(response.text)
urls = re.findall(r'/url\?q=([a-z-A-Z-0-9:/._]+)', ' '.join(parsed_body.xpath('//div[@class="kCrYT"]//a/@href')))
urls = re.sub(r'(\b.*\b)\1', '', ' '.join(urls))  # убираю дубликаты
for url in urls.split():
    response = requests.get(url)  # перехожу по ссылке
    parsed_body = html.fromstring(response.text)
    print(parsed_body.xpath('//title/text()')[0])  # получаю заголовок
