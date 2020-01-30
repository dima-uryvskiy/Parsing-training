import requests
from lxml import html


response = requests.get('https://ru.wikipedia.org/wiki/XPath')
parsed_body = html.fromstring(response.text)
print(parsed_body.xpath('//link[@rel="canonical"]/@href')[0])
