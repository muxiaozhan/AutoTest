# _*_ coding: utf-8 _*_
# __atthor__ = zhengyp
import  os
import sys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.set_window_size(400, 800)
driver.get("http://10.66.30.85:59999/home")
driver.find_element_by_link_text("我的").click()
driver.find_element_by_link_text("点击登录").click()
driver.find_element_by_xpath('// *[ @ id = "sign"] / div[2] / div[2] / div').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]/input').send_keys("15705963365")
sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[2]/input').send_keys("zhang12345")
driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/button').click()
location = (By.XPATH, "/html/body/div[2]")
WebDriverWait(driver, 2, 0.5).until(EC.presence_of_element_located(location))
alert = driver.find_element_by_xpath('/html/body/div[2]')
msg = alert.get_attribute('textContent')
msg = msg.strip()
toastflag = '2'
print(msg+"    "+toastflag)


sleep(3)

driver.close()
'''
def get_toast(browser, click_xpath):  # 获取弹窗信息
    xpath = get_xpath_conf('alert')
    browser.find_element_by_xpath(click_xpath).click()
    try:
        wait(browser, xpath['toast'], 2, 0.5)
        alert = browser.find_element_by_xpath(xpath['toast'])
        msg = alert.get_attribute('textContent')
        msg = msg.strip()
    except:
        try:
            wait(browser,xpath['pop-up'], 2, 0.5)
            msg = browser.find_element_by_xpath(xpath['pop-up']).text
        except:
            msg = '未登录'
    return msg

def wait(browser, xpath, maxs=20, mins=0.5):
    locator = (By.XPATH, xpath)
    WebDriverWait(browser, maxs, mins).until(EC.presence_of_element_located(locator))
'''