"手工处理CSV文件"


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


if __name__ == "__main__":
    CSVReader()

