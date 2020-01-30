import requests
import re
from lxml import html


response = requests.get('https://www.google.com/search?q=xpath')
parsed_body = html.fromstring(response.text)
urls = re.findall(r'/url\?q=([a-z-A-Z-0-9:/._]+)', ' '.join(parsed_body.xpath('//div[@class="kCrYT"]//a/@href')))
urls = re.sub(r'(\b.*\b)\1', '', ' '.join(urls)).split()  # убираю дубликаты

for url in range(1, len(urls) - 1, 2):
    print(urls[url])
