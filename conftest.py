'''
./conftest.py
'''
import pymysql
import pytest
from config.config import *
@pytest.fixture(scope="session", autouse=True)
def destroy_data(sql):
    yield
    sqls = [SQL1, SQL2, SQL3]
    conn = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        db=DB_DB,
        user=DB_USER,
        password=DB_PASSWORD,
        charset='utf8',
        autocommit=True #mysql增删改需要提交事物
    )
    cur = conn.cursor()
    for sql in sqls:
        cur.execute(sql)
    cur.close()
    conn.close()