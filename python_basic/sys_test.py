'''
import sys

print(sys.path)
'''


import json
 
# 테스트용 Python Dictionary
customer = {
    'id': 152352,
    'name': '강진수',
    'history': [
        {'date': '2015-03-11', 'item': 'iPhone'},
        {'date': '2016-02-23', 'item': 'Monitor'},
    ]
}

# JSON 인코딩
jsonString = json.dumps(customer, indent=4)
 
# 문자열 출력
print(jsonString)
print(type(jsonString))   # class str

with open('./20190615python/python_basic/data.json', 'wt') as f:
    f.write(jsonString)