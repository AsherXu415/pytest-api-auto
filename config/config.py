'''
./utils/config.py
'''
# 接口基准地址
BASE_URL = 'http://127.0.0.1:8888/api/private/v1'

# excel格式的测试用例文件配置
EXCEL_FILE = './data/测试用例.xlsx'
SHEET_NAME = 'Sheet1'

# mysql配置
DB_HOST='172.0.0.1 '
DB_PORT=3306
DB_DB='test'
DB_USER='root'
DB_PASSWORD='1234'

#mysql资源销毁
SQL1 = 'delete from "%s"'
SQL2 = 'delete from "%s"'
SQL3 = 'delete from "%s"'
