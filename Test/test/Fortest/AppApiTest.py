#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import os

from muxiaozhan.Test.test.Fortest.Log import WriteLog
from muxiaozhan.Test.test.Fortest.Log import GetConfig

'''
#在接口返回结果中取某个值
phone=respone.json()['data']['phone']
print(phone)
'''
'''
#获取cookies中的token
token=str(respone.cookies)
#split()：把字符串按指定分隔符分割成多个字符串数据
token = token.split('=')[1]
token = token.split(' ')[0]
print(token)
'''


class AppApiTest:
    '''
    #获取cookies
    def GetCookies(self, url, body, headers={"Content-Type": "application/json"}):
        rs = requests.session()
        respone = rs.post(url, headers=headers, data=json.dumps(body))
        return respone.cookies
    '''
    #执行api接口
    def RunApi(self, url, method, body=None, headers={"Content-Type": "application/json"}, cookies=None):
          body = json.dumps(body)
          rq = requests.session()

          if method == "get":
               respone = rq.get(url)
          elif method == "post":
              respone = rq.post(url, data=body, headers=headers, cookies=cookies)
          elif method == "put":
              respone = rq.put(url, data=body, headers=headers, cookies=cookies)
          elif method == "del":
              respone = rq.delete(url, data=body, headers=headers, cookies=cookies)
          return respone, respone.cookies
    #检查接口返回结果
    def Check(self, respone):
      if respone.status_code == 200:
        WriteLog("成功，Status=200")
        print(respone.json())
      else:
        WriteLog("Status:"+str(respone.status_code)+"    "+respone.json()["msg"])
    #读取文件接口信息
    def GetData(self,file):
        file = open(file)
        lines = file.readlines()
        #cookies = self.GetCookies(GetConfig("gzwl_url_test", "AppUrl") + lines[0].split('|')[0],eval(lines[0].split('|')[2]))
        #cookies = apitest.GetCookies(GetConfig("gzwl_url_test","AppUrl")+lines[0].split('|')[0], eval(lines[0].split('|')[2]))
        #api = apitest.RunApi(GetConfig("gzwl_url_test", "AppUrl") + lines[1].split('|')[0], lines[1].split('|')[1], body=eval(lines[1].split('|')[2]), cookies=cookies)
        #print(cookies)
        #print(api.json())
        for line in lines:
            #print(line)
            #cookies = self.GetCookies(GetConfig("gzwl_url_test", "AppUrl") + lines[0].split('|')[0],eval(lines[0].split('|')[2]))
            url = GetConfig("\Data\ApiConfig.conf", "gzwl_url_test", "AppUrl")+line.split('|')[0]
            method = line.split('|')[1]
            body = eval(line.split('|')[2])
            needcookies = line.split('|')[3]
            if needcookies == '1':
                #eval()将字符串str当成有效的表达式来求值并返回计算结果
                api = self.RunApi(url, method, body=body, cookies=cookies)
            else:
                api = self.RunApi(url, method, body=body)
                cookies = api[1]
            self.Check(api[0])
        file.close()


if __name__ == "__main__":
    '''
    url_login = GetConfig("gzwl_url_test","AppUrl")+'/users/authorization/sign-in'
    url1 = GetConfig("gzwl_url_test","AppUrl")+'/home/hot-car'
    url3 = GetConfig("gzwl_url_test","AppUrl")+'/comments/my-comments'
    body_login = {
      "phone": "15705963365",
      "password": "152bf4fe99e450cd2d8f0d7798357cb2c2263f3dc27d9354fa427033ebe397fce704d0c26e34f29d2814b0940360cc241b913b7b880dbc4468c50e44a52f2853704cb2e992c349a7a8723557d2e330ab88d9df4c687fb4ba027e304c92937d11a80818c86c1b01668c629cee3f6b8363e143516ace8d24b32dbdeb0f89eddd22"
    }
    body3 = {
    "paging": {
      "pageIndex": 1,
      "pageSize": 100
    },
    "condition": {
      "type": 0
    }
  }
  '''
    api = AppApiTest()
    #cookies = apitest.GetCookies(url_login,body_login)
    #print(cookies)
    # api3 = apitest.RunApi(url_login,"post",body=body_login,cookies=cookies)
    #print(api3.json())
    # apitest.Check(api3)
    api.GetData("C:\\AutoTest\\muxiaozhan\\Test\\test\Data\\AppApiData.txt")











