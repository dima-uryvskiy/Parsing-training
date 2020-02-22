import requests
from bs4 import BeautifulSoup

url = "http://forum.eve-ru.com/index.php?showtopic=111891"
response = requests.get(url)

soap = BeautifulSoup(response.text, "html.parser")
messages = soap.select("div.post.entry-content")
parsed_messages = [msg.get_text() for msg in messages]
print(*parsed_messages)
