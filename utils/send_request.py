#文件名不要requests,因为存在第三方库requests,不要同名
import allure
import logging
import pymysql
import requests
from config.config import *
#http请求
@allure.step('2、发送http请求')
def send_http_request(**request_data):
    res = requests.request(**request_data)
    logging.info(f"2、发送HTTP请求，响应文本为：{res.text}")
    return res

#JDBC请求
def send_jdbc_request(sql,index=0):
    conn = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        db=DB_DB,
        user=DB_USER,
        password=DB_PASSWORD,
        charset='utf8'
    )
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()

    return result[index]