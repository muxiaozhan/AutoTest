#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/10/25

import requests
import json

from muxiaozhan.Test.test.Fortest.Log import WriteLog
from muxiaozhan.Test.test.Fortest.Log import GetConfig

class BackApiTest:
    #获取token放入headers
    def GetToken(self, url, body, headers={"Content-Type": "application/json"}):
        rs = requests.session()
        respone = rs.post(url, headers=headers, data=json.dumps(body))
        token = respone.json()['data']['sessionId']
        headers = {"Content-Type": "application/json", "token": token}
        return headers
    #运行api接口
    def RunApi(self, url, method, body=None, id="", headers={"Content-Type": "application/json"}):
          body = json.dumps(body)
          rq = requests.session()
          if method == "get":
               respone = rq.get(url)
          elif method == "post":
              respone = rq.post(url, data=body, headers=headers)
          elif method == "put":
              respone = rq.put(url+id, data=body, headers=headers)
          elif method == "del":
              respone = rq.delete(url+id, data=body, headers=headers)
          return respone
    #检查接口返回结果
    def Check(self, respone):
      if respone.status_code == 200:
        WriteLog("成功，Status=200")
        print(respone.json())
      else:
          WriteLog("Status:" + str(respone.status_code) + "    " + respone.json()["msg"])

    #获取文件中的接口信息
    def GetData(self,file):
        file = open(file)
        lines = file.readlines()
        headers = self.GetToken(GetConfig("\Data\ApiConfig.conf", "gzwl_url_test", "BackUrl") + lines[0].split('|')[0],eval(lines[0].split('|')[2]))
        #cookies = apitest.GetCookies(GetConfig("gzwl_url_test","AppUrl")+lines[0].split('|')[0], eval(lines[0].split('|')[2]))
        #api = apitest.RunApi(GetConfig("gzwl_url_test", "AppUrl") + lines[1].split('|')[0], lines[1].split('|')[1], body=eval(lines[1].split('|')[2]), cookies=cookies)
        #print(cookies)
        #print(api.json())
        for line in lines:
            #print(line)
            #headers = self.GetToken(GetConfig("gzwl_url_test", "BackUrl") + lines[0].split('|')[0],eval(lines[0].split('|')[2]))
            url = GetConfig("\Data\ApiConfig.conf", "gzwl_url_test", "BackUrl")+line.split('|')[0]
            method = line.split('|')[1]
            if line.split('|')[2] == '':
                body = None
            else:
                body = eval(line.split('|')[2])
            needtoken = line.split('|')[3]
            id = line.split('|')[4]
            if needtoken == '1':

                #eval()将字符串str当成有效的表达式来求值并返回计算结果
                api = self.RunApi(url, method, body=body, id=id, headers=headers)
            else:
                api = self.RunApi(url, method, body=body, id=id)

            self.Check(api)
        file.close()


if __name__ == "__main__":
    '''
    url_login = GetConfig("gzwl_url_test","BackUrl")+'/backstage-users/sign-in'
    body_login = {
      "userName": "zhangxiaogui",
      "password": "zhang12345"
    }
    api = BackApiTest()
    tooken = api.GetTooken(url_login,body_login)
    print(tooken)
   '''
    api = BackApiTest()
    api.GetData("C:\\AutoTest\\muxiaozhan\\Test\\test\Data\\BackApiData.txt")



