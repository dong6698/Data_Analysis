import json

'''
JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。
Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：
json.dumps(): 对数据进行编码。
json.loads(): 对数据进行解码。
'''

data_1= {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
json_str = json.dumps(data_1)

'''
str()一般是将数值转成字符串。
repr()是将一个对象转成字符串显示，注意只是显示用，有些对象转成字符串没有直接的意思。
如list,dict使用str()是无效的，但使用repr可以，这是为了看它们都有哪些值，为了显示之用。
'''
print ("Python 原始数据：", repr(data_1))
print ("JSON 对象：", json_str)

data_2 = json.loads(json_str)

print("data[no] :", data_2['no'])
print("data[name] :", data_2['name'])
print("data[url]: ", data_2['url'])

'''
如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。

# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)

# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)

'''