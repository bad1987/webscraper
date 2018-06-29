
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

extension_path = "/usr/local/share/chromedriver"

driver = webdriver.Chrome(extension_path)
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://www.youtube.com")

assert "YouTube" in driver.title

search = driver.find_element_by_name("search_query")
search.clear()
search.send_keys("selenium python")

# passwd = driver.find_element_by_name("pass")
# passwd.clear()
# passwd.send_keys("antoine1987")

search.send_keys(Keys.RETURN)

assert "No results found." not in driver.page_source

source = driver.page_source
# driver.close()

soup = BeautifulSoup(source, 'html.parser')
links = soup.find_all('a')
print(links)
# print(soup.prettify())