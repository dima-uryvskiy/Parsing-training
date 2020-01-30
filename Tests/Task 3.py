from lxml import html
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com/search?q=xpath')
page = driver.page_source
parsed_body = html.fromstring(page)
"""
print(*parsed_body.xpath('//div[@class="r"]//a[contains(@ping,"/url?") '
                         'and not(contains(@href,"google"))]/@href'), sep='\n')

"""


print(*parsed_body.xpath('//a[contains(@ping,"/url?") '
                         'and not(contains(@href,"google"))]/@href'), sep='\n')