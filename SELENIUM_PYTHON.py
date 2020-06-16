from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://stihi.ru/")
assert "Стихи" in driver.title
elem = driver.find_element_by_name("string")
elem.clear()
elem.send_keys("автор")
elem.send_keys(Keys.RETURN)
assert "no results found." not in driver.page_source
driver.close()
