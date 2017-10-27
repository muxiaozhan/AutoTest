#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from time import sleep
from muxiaozhan.Test.test.Fortest.Log import GetConfig
from muxiaozhan.Test.test.Fortest.Log import ConnetDb
from muxiaozhan.Test.test.Fortest.Log import WriteLog
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


''' '''
class MyTest(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.set_window_size(400, 800)
        self.driver.get("http://10.66.30.85:59999/home")
        self.driver.find_element_by_link_text("我的").click()
        self.driver.find_element_by_link_text("点击登录").click()

    def login(self, phone, password):
        self.driver.find_element_by_xpath("//input[@type='tel']").clear()
        self.driver.find_element_by_xpath("//input[@type='tel']").send_keys(phone)
        self.driver.find_element_by_xpath("//input[@type='password']").clear()
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        self.driver.find_element_by_xpath("//button[@class='gz-btn']").click()
        sleep(3)

    def is_login_sucess(self):
        if self.check_phone() == 1 & self.check_pwd() ==1:

            text = self.driver.find_element_by_xpath("//div[@class='user-name']").text
            sql = "SELECT user_name from sys_user where phone = " + GetConfig("\Data\\UIConfig.conf", "gzwl_url_test", "phone")
            user_name = ConnetDb(sql)[0][0]
            if self.assertTrue(text, user_name):
                WriteLog("登录成功")
            else:
                WriteLog("登录异常")
        else:
            WriteLog("登录失败：用户名或密码有误")

    def check_phone(self,xpathele):
        if self.driver.find_element_by_xpath(xpathele).text == "请输入正确的手机号":
            WriteLog("手机号码输入不正确")
            phoneflag = 2
        elif self.driver.find_element_by_xpath(xpathele).text == "用户不存在":
            WriteLog("用户不存在")
            phoneflag = 3
        elif self.driver.find_element_by_xpath(xpathele).text == "用户已存在":
            WriteLog("用户已存在")
            phoneflag = 4
        else:
            phoneflag = 1
        return phoneflag

    def check_pwd(self,xpathele):
        if self.driver.find_element_by_xpath(xpathele).text == "请输入正确的密码":
            WriteLog("密码不正确")
            pwdflag = 2
        elif self.driver.find_element_by_xpath(xpathele).text == "密码错误":
            WriteLog("密码错误")
            pwdflag = 3
        else:
            pwdflag = 1
        return pwdflag

    def check_user(self,xpathele):
        if self.driver.find_element_by_xpath(xpathele).text == "用户名格式不正确":
            WriteLog("用户名格式不正确")
            userflag = 2
        else:
            userflag = 1
        return userflag

    def get_toast(self, xpathele):
        try:
            location = (By.XPATH, xpathele)
            WebDriverWait(self.driver, 2, 0.5).until(EC.presence_of_element_located(location))
            alert = self.driver.find_element_by_xpath(xpathele)
            msg = alert.get_attribute('textContent')
            msg = msg.strip()
            toastflag = '2'
            print(msg + "    " + toastflag)
        except:
            toastflag = '1'
        return toastflag

    '''
    def check_code(self):
        if self.driver.find_element_by_xpath('').text == "":
    '''
    def test_login(self):
        phone = GetConfig("\Data\\UIConfig.conf", "gzwl_url_test", "phone")
        pwd = GetConfig("\Data\\UIConfig.conf", "gzwl_url_test", "pwd")
        self.login(phone, pwd)
        self.is_login_sucess()
    '''
    def get_code(self):
    
    def forget
    driver.find_element_by_xpath('// *[ @ id = "sign"] / div[2] / div[2] / div').click()_pwd(self):
        self.
        phone = GetConfig("\Data\\UIConfig.conf", "gzwl_url_test", "phone")
    '''

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":

    unittest.main()

