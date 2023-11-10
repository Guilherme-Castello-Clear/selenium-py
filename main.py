from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, "apexPriceToPay")
# price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
#
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)
#
#
# button = driver.find_element(By.ID, "submit")
# print(button.size)
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

driver.quit()
