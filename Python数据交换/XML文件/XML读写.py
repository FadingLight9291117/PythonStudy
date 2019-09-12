"使用ET解析XML文件(仅供了解)"
import xml.etree.ElementTree as ET
tree=ET.ElementTree(file='./files/pom.xml')
for elem in tree.iter():
    print(elem)