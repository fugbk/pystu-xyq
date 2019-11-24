# encoding = utf-8
__author__ = "Ang Li"

import xml.etree.ElementTree as ET

new_xml = ET.Element("name_list")  # .Element() 创建根节点

# .SubElement(上级节点的对象，本节点名称，attrib={设置属性，字典格式}) 创建子节点
name_1 = ET.SubElement(new_xml, "name", attrib={"id": "10001"})
# age = ET.SubElement(name_1, "age")  # 通过指定上级目录名称，确认层级关系
# age.text = "22"  # 设置属性值
# sex = ET.SubElement(name_1, "sex")
# sex.text = "Man"

# 第二个node ，重复上面操作
name_2 = ET.SubElement(new_xml, "name", attrib={"id": "10002"})
# age = ET.SubElement(name_2, "age")  # 通过指定上级目录名称，确认层级关系
# age.text = "33"  # 设置属性值
# sex = ET.SubElement(name_2, "sex")
# sex.text = "Man"

et = ET.ElementTree(new_xml)  # 生成一个文档对象
et.write("create_xml.xml", encoding="utf-8", xml_declaration=True)  # xml_declaration=True 声明xml格式

ET.dump(new_xml)



# new_xml = ET.Element("namelist")
#
# name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
# age = ET.SubElement(name, "age", attrib={"checked": "no"})
# sex = ET.SubElement(name, "sex")
# sex.text = '33'
#
# name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
# age = ET.SubElement(name2, "age")
# age.text = '19'
#
# et = ET.ElementTree(new_xml)  # 生成文档对象
# et.write("test.xml", encoding="utf-8", xml_declaration=True)
#
# ET.dump(new_xml)  # 打印生成的格式