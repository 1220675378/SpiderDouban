import requests
import re
from fake_useragent import UserAgent
import urllib.robotparser

url = 'https://www.baidu.com'
# 指定ip池
# proxies = {
#     'http': '125.88.74.122:84',
#     'http': '123.84.13.240:8118',
#     'https': '94.240.33.242:3128'
# }
# 指定UA
ua = UserAgent()
headers = {'User-Agent': ua.random}
# print(headers)
# 获取数据
data = requests.get(url, headers=headers)
#  修改编码
# 检测编码
# charset = chardet.detect(data.content)
# 指定编码
# data.encode = charset['encoding']
# print(data.text)
data.encoding = 'utf-8'
data = data.text
# print(data)
titles = re.findall(r'http://.*?.com', data)
print(titles)
# <a href="http://news.baidu.com" target="_blank" class="mnav c-font-normal c-color-t">新闻</a>


