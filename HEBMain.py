import bs4
import pandas as pd
from selenium import webdriver


# chromedriver="C:\Users\user\Desktop\Programming\chromedriver"
driver = webdriver.Chrome()
driver.get("https://www.heb.com/static-page/heb-curbside-delivery")
storename=[]
timeslot=[]

driver.find_element_by_xpath('/html/body/rel/div[2]/div/div/bootstrap/div/div[1]/div/div/footer/button').click() #click OK on HEB initial warning
# df = pd.DataFrame({'Store Name':storename,'timeslot':timeslot})
# df.to_csv('products.csv', index=False, encoding='utf-8')
