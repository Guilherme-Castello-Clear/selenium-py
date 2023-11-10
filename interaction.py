from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()
# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()
#
# search = driver.find_element(By.NAME, "search")
# # print(search.get_attribute("placeholder"))
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

f_name = driver.find_element(By.NAME, "fName")
l_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
button = driver.find_element(By.CLASS_NAME, "btn-block")

f_name.send_keys("Guilherme")
l_name.send_keys("Castello")
email.send_keys("guilherme.castello.clear@gmail.com")
button.click()



# driver.quit()
