# Python——CSV文件读写

---

- 使用标准库 import csv

## CSV文件读取

- 以列表形式读取

```py
# 以列表形式读取CSV
def readbyList():
    with open('./files/CSVTest.csv', 'r', encoding='utf8') as file:
        reader = csv.reader(file)  # 列表形式读取
        data = list(reader)
        print(data)
```
- 以字典形式读取
```py
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
```
