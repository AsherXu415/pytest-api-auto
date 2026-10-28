import jsonpath
import requests

login_data = {
    'method': 'POST',
    'url': 'http://127.0.0.1:8000/login',
    'data':{'username': 'admin', 'password': '123456'},
}

upload_data ={
    'method': 'POST',
    'url': 'http://127.0.0.1:8000/upload',
    'files':None
}

r1 = requests.request(**login_data)
Token = jsonpath.jsonpath(r1.json(),'$..token')[0]



upload_data['headers'] ={'Authorization': Token}
upload_data['files'] = {'file':('1.jpg',open('./files/photo01.jpg','rb'),'jpg')}

#files对应的值类似于{参数名：元组]
#参数名对应在接口文档中的参数名（接口文档）
#参数值元组（参数1，参数2，参数3）
'''
    参数1: 上传服务器时的文件名，
    参数2: 上传文件是个流式操作，用open()函数打开的文件对象
    参数3: 文件类型
'''