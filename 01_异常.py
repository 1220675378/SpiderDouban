import requests
import time

urls = ["http://www.httpstatus.cn/504"]


def get_data(url, num_retries=3):
    try:
        data = requests.get(url)
        print(data.status_code)
    except requests.exceptions.ConnectionError as e:
        print('请求错误：url:', url)
        print('错误详情：', e)
        data = None

    if (data != None) and (500 <= data.status_code < 600):
        if num_retries > 0:
            print("服务器错误正在重试")
            time.sleep(1)
            num_retries -= 1
            get_data(url, num_retries)
    return data


if __name__ == '__main__':
    for url in urls:
        get_data(url)
