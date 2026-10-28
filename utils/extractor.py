'''
./utils/extractor.py
'''
import jsonpath
from setuptools import logging
from utils.send_request import send_jdbc_request
import allure
import logging
def json_extractor(case,all,r): #参数出现顺序，1、case 2、函数内引用全局变量all 3、响应r
    if case['jsonExData']:
        with allure.step('4、json提取'):
            for key, value in eval(case['jsonExData']).items():
                value = jsonpath.jsonpath(r.json, value)[0]
                all[key] = value
            logging.info(f"4、JSON提取，根据{case['jsonExData']}提取信息，此时全局变量为{all}")

def jdbc_extractor(case,all,r):
    if case['sqlExData']:
        with allure.step('4、JDBC提取'):
            for key, value in eval(case['sqlExData']).items():
                value = send_jdbc_request(value)
                all[key] = value
            logging.info(f"4、JDBC提取，根据{case['sqlExData']}提取信息，此时全局变量为{all}")