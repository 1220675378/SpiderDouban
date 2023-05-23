"""
@Project ：_爬虫 
@File    ：testbs4.py
@IDE     ：PyCharm 
@Author  ：lbw
@Date    ：2023/05/19 15:01 
"""
import chardet
from bs4 import BeautifulSoup
import requests
import re

url = 'http://www.baidu.com'
data = requests.get(url)
# 转换编码格式
charset = chardet.detect(data.content)
data.encoding = charset['encoding']

bs = BeautifulSoup(data.text, 'html.parser')


# print(bs.title.string)
# print(bs)


# ---------------------
# 文档的遍历
# print(bs.contents)
# 文档的搜索
# 正则表达式搜索
# t_list = bs.find_all(re.compile(r'a'))
# print(t_list)


# def name_is_exist(tag):
#     return tag.has_attr('name')
#
#
# t_list = bs.find_all(name_is_exist)
# for item in t_list:
#     print(item)

t_list = bs.find_all(id='head')
print(t_list)











