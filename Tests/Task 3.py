from lxml import html
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com/search?q=xpath')
page = driver.page_source
parsed_body = html.fromstring(page)

print(*parsed_body.xpath('//div[@class="rc"]/div[@class="r"]/a/@href'), sep='\n')
