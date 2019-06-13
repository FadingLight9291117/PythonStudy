"JSON与Python数据结构相互转换，以及文件IO操作"
import json


# 将python数据结构转换为JSON
# 将JSON转换为Python数据结构
def fun1():
    data = {'name': 'nick', 'age': 12}
    data_json = json.dumps(data)  # dict对象转换为JSON(字符串)

    data2 = json.loads(data_json)  # JSON(字符串)转换为一个dict对象

    print(type(data_json))
    print(data_json)
    print(type(data2))
    print(data2)


# 写入JSON文件
def fun2():
    data = {'name': 'nick', 'age': 12}
    with open('./files/data.json', 'w', encoding='utf8') as file:
        json.dump(data, file)  # 直接就将字符串转换为JSON并写入文件


# 读取JSON文件
def fun3():
    with open('./files/data.json', 'r', encoding='utf8') as file:
        data = json.load(file)  # 将JSON转换为dict对象返回
        print(type(data))  # 返回一个dict对象
        print(data)


if __name__ == "__main__":
    fun1()
    # fun2()
    # fun3()
