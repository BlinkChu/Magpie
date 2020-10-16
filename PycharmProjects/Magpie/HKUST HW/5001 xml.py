import re

xml_content = ""
with open('/Users/blinkchu/Downloads/blocklist.xml','r') as f:
    xml_content = f.read()

# print(xml_content)

block_pattern = '(?P<blockid><emItem blockID="i\d+" id="{.+}">)'
blockid_lst = re.findall(block_pattern,xml_content)

ID_pattern = '(?P<blockid><emItem blockID=".+" id=".+@.+">)'
emails_lst = re.findall(ID_pattern,xml_content)

# for i in emails_lst:
#     if not (('/' in i) or ('/' in i) or ('^' in i)):
#         print(i)

for i in blockid_lst:
    print(i)