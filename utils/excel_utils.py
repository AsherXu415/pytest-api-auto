import openpyxl
from config.config import *

def read_excel(file_path=EXCEL_FILE,sheet_name=SHEET_NAME):
    # 打开文件
    workbook = openpyxl.load_workbook(file_path)  # 参数传文件路径

    # 选择sheet页
    worksheet = workbook[sheet_name]

    # 创建空列表，用于组装字典，将data放入数据参数化方法中
    data = []

    # 获取请求信息的key,方法一
    # for cell in worksheet[2]:
    #     cell.value

    # 获取请求信息的key,方法二，列表生成式
    keys = [cell.value for cell in worksheet[2]]

    # 获取请求信息的value
    for row in worksheet.iter_rows(min_row = 3,values_only=True):
        # 利用zip（）函数组装
        dict_data = dict(zip(keys,row))
        print(dict_data['is true'])
        #判断是否执行，执行就添加测试数据到data中
        if dict_data['is true']:
            data.append(dict_data)

    # 关闭excel
    workbook.close()
    return data

if __name__ == '__main__':
    data = read_excel()
    print(data)