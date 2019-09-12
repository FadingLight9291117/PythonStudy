"SQLite3数据库存取"
from faker import Faker
import sqlite3
fake = Faker("zh-cn")
# 创建在内存上
# with sqlite3.connect(':memory:') as conn
# 创建在硬盘上
with sqlite3.connect('./files/test.db') as conn:
    # 创建游标
    c = conn.cursor()
    # 创建表如果不存在
    c.execute(
        "create table if not exists user (id integer primary key autoincrement ,name varchar(20))")
    # # 插入数据
    # for i in range(10):
    #     c.execute("insert into user (name) values ('{}')".format(fake.name()))
    # # 事务提交
    # conn.commit()
    c.execute("select * from user")
    result = c.fetchall()
    print(type(result))
    print(result)
