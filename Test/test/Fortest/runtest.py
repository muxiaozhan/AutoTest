#!/usr/bin/env python
# -*- coding: utf-8 -*-

from muxiaozhan.Test.test.Fortest.AppApiTest import AppApiTest
from muxiaozhan.Test.test.Fortest.BackApiTest import BackApiTest
import os
from muxiaozhan.Test.test.Fortest.Log import ConnetDb
from muxiaozhan.Test.test.Fortest.Log import GetConfig
from muxiaozhan.Test.test.Fortest.Log import WriteLog

#appapi = AppApiTest()
#appapi.GetData("C:\\AutoTest\\muxiaozhan\\Test\\test\Data\\AppApiData.txt")

#backapi = BackApiTest()
#backapi.GetData("C:\\AutoTest\\muxiaozhan\\Test\\test\Data\\BackApiData.txt")

sql = "SELECT user_name from sys_user where phone = "+GetConfig("\Data\\UIConfig.conf", "gzwl_url_test", "phone")
name = ConnetDb(sql)
if name[0][0] == "IamZhangXiao桂123":
    print(name[0][0])
else:
    print("name is wrong")
