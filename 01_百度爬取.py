import re
import time
import chardet
import urllib.robotparser
import requests
from fake_useragent import UserAgent


# 获取headers
def get_headers():
    ua = UserAgent()
    headers = {'User-agent': ua.random}
    return headers


# robots.txt检测
def robots_check(robotstxt_url, headers, url):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robotstxt_url)
    rp.read()
    result = rp.can_fetch(headers['User-Agent'], url)
    return result


# 获取网页数据
def get_data(url, num_retries=3):
    try:
        data = requests.get(url, timeout=5, headers=get_headers())
        print(data.status_code)
    except requests.exceptions.ConnectionError as e:
        print("请求错误,url:", url)
        print("错误详情:", e)
        data = None
    except:  # other exceptions
        print("未知错误，url", url)
        data = None
    if (data is not None) and (500 <= data.status_code < 600):
        if num_retries > 0:
            print("服务器错误重试中")
            time.sleep(1)
            num_retries -= 1
            get_data(url, num_retries)
    return data


# 解析网页内容
def parse_data(data):
    if data is None:
        return None
    charset = chardet.detect(data.content)
    data.encoding = charset['encoding']
    html_text = data.text
    '''
    对网页数据进行解析提取
    '''
    title_text = re.findall(r'<title>(.*?)</title>', html_text)
    return title_text


if __name__ == '__main__':
    data = get_data("https://www.baidu.com")
    request_text = parse_data(data)
    print(request_text)