import xml.etree.ElementTree as ET
import pandas as pd

employee = ET.Element("employee")
details = ET.SubElement(employee, "details")
first = ET.SubElement(details, "first_name")
last = ET.SubElement(details, "last_name")
age = ET.SubElement(details, "age")

first.text = "Mark"
last.text = "abc"
age.text = "27"

tree = ET.ElementTree(employee)
with open("read_and_write_xml_file/person_info.xml", "wb") as file:
    file.write(b"<?xml version='1.0' encoding='utf-8'?>\n")
    tree.write(file)

new_tree = ET.parse("read_and_write_xml_file/person_info.xml")
root = new_tree.getroot()
columns = ["first_name", "last_name", "age"]

rows = []
for node in root:
    rows.append([node.find(col).text for col in columns])

df = pd.DataFrame(rows, columns=columns)
print(df)