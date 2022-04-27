import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = 'https://baomoi.com/'
search_input='input[type="text"]'
search_text="Ronaldo"
page_detail_url='h4.bm_L > span a[href="/mua-giai-tham-hoa-cua-man-united/c/42436117.epi"]'

def test_search_bao():
  driver.get(url)
  time.sleep(1)

  search_el = driver.find_element(by=By.CSS_SELECTOR, value=search_input)
  search_el.send_keys(search_text)
  time.sleep(1)
  search_el.send_keys(Keys().RETURN)
  time.sleep(2)

  driver.find_element(by=By.CSS_SELECTOR, value=page_detail_url).click()
  time.sleep(4)

  driver.close()

test_search_bao()