'''
封装函数放在工具utils下面
./utils/allure_utils.py
case只是传参，不代表实际case，这里的case可以是任何形参
def allure_init(a):
    allure.dynamic.feature(a['feature'])
    allure.dynamic.story(a['story'])
    allure.dynamic.title(f'ID:{a["id"]}--Title:{a["title"]}')
'''
import allure

def allure_init(case):
    allure.dynamic.feature(case['feature'])
    allure.dynamic.story(case['story'])
    allure.dynamic.title(f'ID:{case["id"]}--Title:{case["title"]}')