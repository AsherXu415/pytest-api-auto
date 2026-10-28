import pytest
import os



#--alluredir ./report/test 指定一个目录，并生成中间结果
#-- clean-alluredir 每次运行会清空中间结果
if __name__ == "__main__":
    pytest.main(['-vs','./testcases/test_runner.py','--alluredir','./report/json_report','--clean-alluredir'])

    #os.system(命令)相当于在cmd中执行命令
    #allure generate中间结果目录 -o 目标html报告目录 --clean
    os.system('/Users/xuxiubin/allure/bin/allure generate ./report/json_report -o ./report/html_report --clean')