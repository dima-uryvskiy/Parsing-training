from pathlib import Path
import requests
from bs4 import BeautifulSoup

url = "http://forum.eve-ru.com/index.php?showtopic=111891"
response = requests.get(url)

soap = BeautifulSoup(response.text)

