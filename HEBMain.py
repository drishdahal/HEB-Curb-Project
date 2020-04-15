import bs4
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.heb.com/static-page/heb-curbside-delivery")
storename = []
timeslot = []


#need to wait until it pops up, need to change code later for it to click anywhere on the screen to continue
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "once-per-session___BV_modal_footer_"))
 )

driver.find_element_by_xpath('/html/body/rel/div[2]/div/div/bootstrap/div/div[1]/div/div/footer/button').click() #click OK on HEB initial warning
driver.find_element_by_xpath('/html/body/rel/div[2]/div/div/div[2]/header/div[2]/div[2]/div[2]/div[1]/div/bootstrap/div/button').click() #click on reserve time slot

#need to wait until new window pops up
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "change-timeslot-modal___BV_modal_content_"))
 )
changeStore = driver.find_element_by_xpath('/html/body/rel/div[2]/div/div/div[2]/header/div[2]/div[2]/div[2]/div[1]/div/bootstrap/bootstrap/div[1]/div[1]/div/div/div/div/div[2]/div[1]/div[1]/button')

changeStore.click() #click on change store

#Now, writing zipcode on the text box then hitting enter
zipcodeBox = driver.find_element_by_xpath('/html/body/rel/div[2]/div/div/div[2]/header/div[2]/div[2]/div[2]/div[1]/div/bootstrap/bootstrap/div[3]/div[1]/div/div/div/form/input')
zipcodeBox.send_keys('78256')
zipcodeBox.send_keys(Keys.ENTER)


# df = pd.DataFrame({'Store Name':storename,'timeslot':timeslot})
# df.to_csv('products.csv', index=False, encoding='utf-8')