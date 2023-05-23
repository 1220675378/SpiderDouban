"""
@Project ：_爬虫 
@File    ：testurllib.py
@IDE     ：PyCharm 
@Author  ：lbw
@Date    ：2023/05/19 11:59 
"""

import urllib.parse
import urllib.request
import requests
# 获取一个get请求
# request_data = urllib.request.urlopen("http://httpbin.org/get")
# print(request_data.read().decode("utf-8"))

# 获取一个post请求
# redata = requests.post("http://httpbin.org/post")
# print(redata.text)

# data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding="utf-8")
# post_data = urllib.request.urlopen("http://httpbin.org/post", data= data)
# print(post_data.read().decode("utf-8"))
# 超时处理
# try:
#     request_data = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(request_data.read().decode("utf-8"))
# except Exception as e:
#     print(e)

# 响应头
# data = urllib.request.urlopen("http://httpbin.org/get")
# print(data.getheaders())

# 浏览器伪装
# url = "http://httpbin.org/post"
headers = {
    "UserAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Refere":"https://www.douban.com/"
}

# data = bytes(urllib.parse.urlencode({"name":"aaa"}),encoding="utf-8")
# data = urllib.request.Request(url, headers=headers,data=data,method="POST")
# res = urllib.request.urlopen(data)
# print(res.read().decode('utf-8'))
# 访问豆瓣   https://www.douban.com/
url = 'https://www.douban.com'
# data = urllib.request.Request(url, headers=headers)
# req = urllib.request.urlopen(data)
# print(req.read().decode('utf-8'))

data = requests.get(url, headers=headers)
print(data.status_code)










