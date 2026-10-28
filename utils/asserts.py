'''
.utils/asserts.py
'''
import allure
import jsonpath
from utils.send_request import send_jdbc_request
import logging

@allure.step('3、http响应断言')
# 封装http断言
def http_assert(case,r,index=0):
    if case['check']:
        result = jsonpath.jsonpath(r.json(), case['check'])[index]
        logging.info(f"3、HTTP响应断言内容：实际结果:({result}) == 预期结果:({case['expected']})")
        # 校验字段和预期结果比较，利用jsonpath函数取值，返回是个列表要加【0】取第一个值
        assert result == case['expected']
    else:
        logging.info(f"3、HTTP响应断言内容：预期结果:({case['expected']}) in 实际结果:({r.text})")
        # 校验字段是空的，预期结果是否包含在返回结果中，r.json()是字典类型，不能和字符串做比较，需要用r.text是字符串类型
        assert case['expected'] in r.text

#@allure.step('3、jdbc响应断言')装饰器需要优化，测试用例中有部分用例不需要数据库断言，allure报告step中不需要该步骤
# 封装jdbc断言
def jdbc_assert(case):
    if case['sql_check'] and case['sql_expected']:
        # 优化方法：with allure.step('步骤描述')：用于函数内部，且allure报告->功能->step会显示步骤，但不会显示传参
        with allure.step('3、jdbc响应断言'):
            # 调用封装JDBC请求
            result = send_jdbc_request(case['sql_check'])
            logging.info(f"3、jdbc响应断言内容：实际结果:({result}) == 预期结果:({case['sql_expected']})")
            assert result == case['sql_expected']
