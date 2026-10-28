import pytest
from setuptools import logging
from utils.excel_utils import read_excel
from jinja2 import Template
from utils.allure_utils import allure_init
from utils.analyse_case import analyse_case
from utils.asserts import http_assert,jdbc_assert
from utils.send_request import send_http_request
from utils.extractor import json_extractor, jdbc_extractor
import logging

class TestRunner:
    all = {}
    data =  read_excel()

    @pytest.mark.parametrize('case',data)
    def test_case(self,case):



        # 引用all（建立测试函数内外all变量的对应关系）
        all = self.all

        # 模版渲染
        case = eval(Template(str(case)).render(all))
        '''
            1.Template需要字符串，data是用例列表，循环取出的case是列表里的字典
            2.excel单元格读取都是字符串，headers写模板：{"Authorization":"{{Token}}"}
            3.all是字典，存放全局变量（如Token）；str(case)把字典转为字符串，交给模板渲染
            4.eval将渲染后的字符串还原成字典
        '''
        # 封装allure报告
        allure_init(case)

        # 0.测试用例的描述信息的日志
        logging.info(f"0、用例ID：{case['id']}模块：{case['feature']}场景：{case['story']}标题:{case['title']}")

        # 核心步骤1：解析请求数据
        request_data = analyse_case(case)

        # 核心步骤2：发起请求，得到响应结果
        r = send_http_request(**request_data)

        # 核心步骤3：返回值校验，数据库校验
        http_assert(case,r)
        jdbc_assert(case)

        # 核心步骤4：json提取,数据库提取
        json_extractor(case,all,r)
        jdbc_extractor(case,all,r)






