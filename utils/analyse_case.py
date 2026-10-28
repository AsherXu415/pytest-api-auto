'''
    存放路径./utils/analyse_case.py
'''
import allure
import logging
from config.config import BASE_URL
#使用装饰器，显示allure报告->功能,添加执行中的测试步骤：@allure.step('步骤描述')
@allure.step('1、解析请求数据')
def analyse_case(case):
    # 数据解析：1.URL不存在 2.字典内部分value是string需要变成字典 3.excel表格中的预期结果不能再请求中传输，会报错
    method = case['method']
    url = BASE_URL + case['path']
    params = eval(case['params']) if isinstance(case['params'], str) else None
    data = eval(case['data']) if isinstance(case['data'], str) else None
    files = eval(case['files']) if isinstance(case['files'], str) else None
    json = eval(case['json']) if isinstance(case['json'], str) else None
    headers = eval(case['headers']) if isinstance(case['headers'], str) else None

    request_data = {
        'method': method,
        'params': params,
        'data': data,
        'files': files,
        'json': json,
        'headers': headers,
        'url': url
    }
    logging.info(f"1、解析请求数据，请求数据为：{request_data}")
    allure.attach(f'{request_data}',name='解析数据的结果')
    #需要加上返回值
    return request_data