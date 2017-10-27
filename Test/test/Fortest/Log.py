#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import logging.config
import os
import configparser
import pymysql
'''

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a,%d %b %Y %H:%M:%S',
                    filename='/AutoTest/Test/Log/Fortest.log',
                    filemode='w')
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
'''
'''

#1.创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger1 = logging.getLogger()

#2.创建一个handler，用于写入日志文件/输出到控制台
#向控制台中输出日志
ch = logging.StreamHandler()
# 向一个文件输出日志
fh = logging.FileHandler('/AutoTest/Test/Log/test1.log')

#logging.handlers.RotatingFileHandler向文件中输出日志，当文件达到一定大小后，自动 更改当前日志文件，创建一个新的同名日志文件继续输出
#logging.handlers.TimedRotatingFileHandler向文件中输出日志，间隔一定时间就自动创建新的日志文件

3.定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

4.logger添加到handler里面
#logger.addHandler(fh)
logger.addHandler(ch)
#logger1.addHandler(fh)
#logger1.addHandler(ch)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.critical('logger critical message')

logger1.debug('logger1 debug message')
logger1.info('logger1 info message')
logger1.warning('logger1 warning message')
logger1.critical('logger1 critical message')
'''


#获取配置文件信息
def GetConfig(file, section, option):
    # 获取当前文件所在的文件夹的上级文件夹目录
    frontdir = os.path.dirname(os.getcwd())
    conf = configparser.ConfigParser()
    conf.read(frontdir + file)
    return conf.get(section, option)
'''
def ReadConfig(file, section, option):
    conf = configparser.ConfigParser()
    conf.read(file)
    return conf.get(section, option)
'''

#记录日志
def WriteLog(msg, level="debug",loggername = "Example"):
    frontdir = os.path.dirname(os.getcwd())
    #从指定的文件目录中读取logging配置文件
    logging.config.fileConfig(frontdir + "\Data\ApiConfig.conf")
    logger = logging.getLogger(loggername)
    if level == "debug":
        logger.debug(msg)
    elif level == "info":
        logger.info(msg)
    elif level == "warning":
        logger.warning(msg)
    else:
        logger.error("有错误，日志:" + msg)


#链接数据库
def ConnetDb(sql):
    db_host = GetConfig("\Data\ApiConfig.conf", "gzwl_db_test", "db_host")
    db_user = GetConfig("\Data\ApiConfig.conf", "gzwl_db_test", "db_user")
    db_pwd = GetConfig("\Data\ApiConfig.conf", "gzwl_db_test", "db_pwd")
    db = GetConfig("\Data\ApiConfig.conf", "gzwl_db_test", "db")
    mysqldb = pymysql.connect(db_host, db_user, db_pwd, db, charset='utf8')
    cursor = mysqldb.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


if __name__ == "__main__":
    sql = "SELECT id,user_name,phone from sys_user where is_delete='0' and phone='15705963365'"
    print(ConnetDb(sql)[0][2])
    WriteLog("ceshi")

