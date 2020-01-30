from lxml import html
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com/search?q=xpath')
page = driver.page_source
parsed_body = html.fromstring(page)
print(*parsed_body.xpath('//h3[@class="LC20lb"]/text()'), sep='\n')


#  XPath = '//h3[@class="LC20lb"]/text()'