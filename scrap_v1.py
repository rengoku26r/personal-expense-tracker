from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
import time
from captcha import getText
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get("bank")

internetBanking = driver.find_element(by=By.LINK_TEXT, value="")
time.sleep(4)
internetBanking.click()

continueBtn = driver.find_element(by=By.CLASS_NAME,value="")

ActionChains(driver)\
    .send_keys("ID")\
    .perform()

time.sleep(4)
continueBtn.click()
time.sleep(4)

ActionChains(driver)\
    .send_keys("Pass")\
    .perform()

img_element = driver.find_element(by=By.ID, value="")
img_element.screenshot("captcha.png")
captchaKeys = getText("captcha.png")

ActionChains(driver)\
    .send_keys(captchaKeys)\
    .key_down(Keys.ENTER)\
    .perform()

alert = WebDriverWait(driver,10).until(EC.alert_is_present())
alert.accept()

time.sleep(10)

statement = driver.find_element(by=By.LINK_TEXT, value="")
time.sleep(4)
statement.click()

time.sleep(10)