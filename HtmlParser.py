import xml.etree.ElementTree as ET
import json

tree = ET.parse('1050812_行政區經緯度(toPost).xml')
root = tree.getroot()

data_arr = []

for child in root:
    data = {}
    # for entry in child:
    #     print(entry.tag, entry.text)
    data['name'] = child.find('行政區名').text
    data['lat'] = child.find('中心點經度').text
    data['lng'] = child.find('中心點緯度').text
    data['post'] = child.find('_x0033_碼郵遞區號').text
    data_arr.append(data)
    print(data['name'])

json_str = json.dumps(data_arr, ensure_ascii=False, indent=2)
f = open("taiwan_dist_2021_july.json", "w", encoding='utf16')
f.write(json_str)
f.close()