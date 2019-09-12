"使用csv标准库处理csv文件"
import csv


# 以列表形式读取CSV
def readbyList():
    with open('./files/CSVTest.csv', 'r', encoding='utf8') as file:
        reader = csv.reader(file)  # 列表形式读取
        data = list(reader)
        print(data)


# 以列表形式写入CSV
def writebyList():
    keys = ['a', 'b', 'c', 'd']
    data = [[1, 2, 3, 4], [5, 6, 7, 8], [11, 22, 33, 44]]
    with open('./files/CSVTest3.csv', 'w', encoding='utf8') as file:
        writer = csv.writer(file,lineterminator='\n')  # 设置待写入文件
        writer.writerow(keys)  # 写入索引
        # writer.writerows(data)#一次写入多个数据
        for row in data:  # 一行一行写入数据
            writer.writerow(row)


# 以字典形式读取CSV
def readbyDict():
    with open('./files/CSVTest.csv', 'r', encoding='utf8', newline='') as file:
        reader = csv.DictReader(file)  # 字典形式读取
        fieldnames = reader.fieldnames  # 获取列索引
        print(fieldnames)
        data = list()
        for row in reader:
            data.append(dict(row))
        print(data)


# 以字典形式写入CSV
def writebyDict():
    fieldname = ['a', 'b', 'c', 'd']
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 12}, {'a': 4, 'b': 5,
                                                'c': 6, 'd': 21}, {'a': 7, 'b': 8, 'c': 9, 'd': 21}]
    with open('./files/CSVTest4.csv', 'w', encoding='utf8') as file:
        writer = csv.DictWriter(
            file, fieldnames=fieldname,lineterminator='\n')  # 设置读取文件同时设置域名/列索引
        writer.writeheader()  # 写入头/域名/列索引
        writer.writerows(data)  # 全部写入数据


if __name__ == "__main__":
    # writebyList()
    # writebyDict()
    readbyDict()
