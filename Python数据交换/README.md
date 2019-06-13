# Python数据交换

    关于CSV，Excel，JSON，PDF，JSON，XML，数据库等文件的读写操作。

## 一. 普通文件读写

**具体步骤**

1. 打开文件：
    * <变量名> = open(<文件名>,<打开模式>)
2. 文件操作：
   * 读或写
3. 关闭文件：
   * <变量名> = close()

**但是**

推荐使用上下文管理器*with*语句打开文件，省去了关闭文件操作。

``` python
# 举个例子
a=open('../file.txt','w',encoding='utf-8') # 打开文件
a.write("test") # 文件操作
a.close() # 关闭文件

#推荐的with语句
with open = ('../file.txt','w',encoding='utf=8') as file:
    pass # 文件具体操作
```

---

- 文件打开模式

    | 文件打开模式 |                         描述                          |
    | :----------: | :---------------------------------------------------: |
    |     'r'      |  只读模式，默认，若文件不存在，返回FileNotFoundError  |
    |     'w'      |      覆盖写，若不存在则创建文件，存在则覆盖原文       |
    |     'x'      | 创建写，若不存在则创建文件，存在则返回FileExistsError |
    |     'a'      | 追加写，若不存在则创建文件，存在则在文件内容后追加写  |
    |     'b'      |                      二进制模式                       |
    |     't'      |                   文本模式，默认值                    |
    |     '+'      |  与r/w/x/a/一同使用，在原功能基础上增加同时读写功能   |

---

- 文件读取操作函数

    |         函数名         |                       描述                       |
    | :--------------------: | :----------------------------------------------: |
    |   <f>.read(size=-1)    |    读入全部内容并返回，若有参数读入前size长度    |
    | <f>.readline(size=-1)  | 读入一行内容并返回，若有参数，读入该行前size长度 |
    | <f>.readlines(hint=-1) | 读入所有行并返回一个列表，若有参数，读入前hint行 |

---

- 文件写入操作函数

    |        函数名         |                                               描述                                                |
    | :-------------------: | :-----------------------------------------------------------------------------------------------: |
    |     <f>.write(s)      |                                      写入一个字符串或字节流                                       |
    | <f>.writelines(lines) |                            将一个元素全为字符串的列表拼接后，写入文件                             |
    |   <f>.seek(offset)    | 改变当前文件操作指针的位置，offset含义如下:<br>0 - 文件开头；<br>1 - 当前位置；<br>2 - 文件结尾。 |


## 二. CSV文件

    Common Separateed Values 国际通用一二维数据存储格式，扩展名为.csv

**文件格式如下：**

```cs
城市,环比,同比,定基
北京,101.5,120.7,121.4
上海,101.2,127.3,127.8
广州,101.3,119.4,120.0
深圳,102.0,140.9,145.5
沈阳,100.1,101.4,101.6
```

---

### 1. 手工处理CSV文件

见[普通文件的读写]()。

**例如**

```python
# 手工读取CSV文件
def CSVReader():
    with open('./files/CSVTest.csv', 'r', encoding='utf8') as file:  # 注意设置字符集为utf8才可读取中文
        ls = []
        for line in file:
            line = line.strip()
            ls.append(line.split(","))
        print(ls)
        return ls


# 写入CSV文件
def CSVWriter():
    with open('./files/CSVTest2.csv', 'w', encoding='utf8') as file:
        ls = CSVReader()
        for item in ls:  # 按行写入
            file.write(','.join(item)+'\n')
```

---

### 2. 使用CSV标准库

```python
import csv
```

- **List形式读写**

    - 首先初始化csv库（*设置文件句柄*）

        reader=csv.reader(file)

        writer=csv.writer(file)

        |      函数名      |                      描述                      |
        | :--------------: | :--------------------------------------------: |
        | csv.writer(file) | 设置读取文件句柄，file为文件句柄，返回文件对象 |
        | csv.reader(file) | 设置写入文件句柄，file问文件句柄，返回数据对象 |

    - 读操作

        使用*for*循环逐行读取

        ```python
        for row in reader:
            print(row)
        ```

    - 写操作

        |         函数名         |             描述             |
        | :--------------------: | :--------------------------: |
        |  reader.writerow(row)  | 写入一行数据，row为一维列表  |
        | reader.writerows(data) | 写入多行数据，data为二维列表 |

- **dict形式读写**

    - 首先初始化csv库（*设置文件句柄*）

        csv.DictWriter(file,fieldnames)

        csv.DictReader(file)

        |             函数名              | 描述                                               |
        | :-----------------------------: | :------------------------------------------------- |
        | csv.DictWriter(file,fieldnames) | file为文件句柄，fieldnames为数据索引，返回文件对象 |
        |      csv.DictReader(file)       | file为文件句柄，返回数据对象                       |

    - 读操作

        |      函数名       |     描述     |
        | :---------------: | :----------: |
        | reader.fieldnames() | 返回索引列表 |
        
        循环获取数据列表

        ```python
        for row in reader:
            print(row)
        ```

    - 写操作

        |         函数名         |           描述           |
        | :--------------------: | :----------------------: |
        |  writer.writeheader()  |  写入索引，即fieldnames  |
        | writer.writerows(data) | 写入数据，data为二维List |

**举例**
```python
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
        writer = csv.writer(file)  # 设置待写入文件
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
    data = [{'a':1,'b':2,'c':3,'d':12},{'a':4,'b':5,'c':6,'d':21},{'a':7,'b':8,'c':9,'d':21}]
    with open('./files/CSVTest3.csv', 'w', encoding='utf8') as file:
        writer = csv.DictWriter(
            file, fieldnames=fieldname)  # 设置读取文件句柄同时设置域名/列索引
        writer.writeheader()#写入头/域名/列索引
        writer.writerows(data)#全部写入数据
```