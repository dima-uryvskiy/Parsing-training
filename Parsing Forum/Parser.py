from pathlib import Path
import requests

url = "http://forum.eve-ru.com/index.php?showtopic=111891"
response = requests.get(url)


base_path = Path("./Forum file")
html_file_path = base_path / "first.html"

with open(str(html_file_path.absolute()), "wb") as f:
    f.write(response.content)
