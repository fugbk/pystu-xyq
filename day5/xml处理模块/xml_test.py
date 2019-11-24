# encoding = utf-8
__author__ = "Ang Li"

import xml.etree.ElementTree as ET

tree = ET.parse("xmltest.xml")  # 先打开一个xml文件
root = tree.getroot()  # 这里获取的是这个打开文件的内存对象
print(root.tag)  # root.tag 是这个xml文件的根标签的名字

def create_xml():
    """
    创建xml文档，创建文档就不需要先打开文件了，最后写入即可。
    整个xml文档，其实就是一个个的节点组成，每个节点包含有 “标签名”，“属性（字典）”，“value值”
    还可以有下级标签
    :return:
    """
    new_xml = ET.Element("name_list")  # .Element() 创建根节点

    # .SubElement(上级节点的对象，本节点名称，attrib={设置属性，字典格式}) 创建子节点
    name_1 = ET.SubElement(new_xml, "name", attrib={"id": "10001"})
    name_1.text = "Tom"
    age = ET.SubElement(name_1, "age")  # 通过指定上级目录名称，确认层级关系
    age.text = "22"  # 设置属性值
    sex = ET.SubElement(name_1, "sex")
    sex.text = "Man"

    # 第二个node ，重复上面操作
    name_2 = ET.SubElement(new_xml, "name", attrib={"id": "10002"})
    name_2.text = "Jerry"
    age = ET.SubElement(name_2, "age")  # 通过指定上级目录名称，确认层级关系
    age.text = "33"  # 设置属性值
    sex = ET.SubElement(name_2, "sex")
    sex.text = "Man"

    et = ET.ElementTree(new_xml)  # 生成一个文档对象
    et.write("create_xml.xml", encoding="utf-8", xml_declaration=True)  # xml_declaration=True 声明xml格式

    ET.dump(new_xml)

create_xml()


def change_xml():
    """
    修改xml文件，year + 1 ，添加修改人属性
    :return:
    """
    for year in root.iter("year"):
        old_year = int(year.text)  # xml 中存入的是 str 格式
        new_year = old_year + 1
        year.text = str(new_year)  # 修改year.text 需要一str 格式
        year.set("update_by", "ali") # 添加属性 update_by=ali, 属性的添加要用.set()
    tree.write("xmltest.xml")


def traverse():
    """
    全文遍历的方式，解析xml 文件
    :return:
    """
    for child in root:  # 这里的root是打开的内存对象，而循环root 其实就是循环 根标签下的二级标签
        print(child.tag, child.attrib)  # .tag 表示“标签名”， .arrtib 表示“标签属性”

        # 使用同样的方法，获取所有标签内信息
        for i in child:
            if i.tag == "neighbor":
                print(i.attrib["name"], i.attrib["direction"])
            else:
                print(i.tag, i.text)


def select_node():
    """
    查找指定节点，精准遍历
    :return:
    """
    for country in root.iter('country'):  # .iter() 指定一个标签
        for gpdpc in country.iter("gdppc"):
            print(country.attrib["name"], gpdpc.text)

