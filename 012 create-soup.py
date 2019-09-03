from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path = r'/usr/bin/chromedriver')


driver.get('http://python.org')

html_doc  = driver.page_source

soup = BeautifulSoup(html_doc, 'lxml')

print(soup.prettify())
driver.quit()
