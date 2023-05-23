"""
@Project ：_爬虫
@File    ：spider.py
@IDE     ：PyCharm 
@Author  ：lbw
@Date    ：2023/05/18 19:04 
"""
from bs4 import BeautifulSoup
import urllib.request
import xlwt
import re


# 爬取url
def main():
    url = 'https://movie.douban.com/top250?start='
    datalist = getData(url)
    savePath = ".\\豆瓣电影Top250.xls"
    saveData(datalist,savePath)
# 定义全局正则表达式
# 正则提取链接
findlink = re.compile(r'<a href="(.*?)">')
# 正则提取图片路径
findImg = re.compile(r'<img.*src="(.*?)".*?>',re.S) #re.s 让换行符包含在字符中
# 正则提取名称
findtitle = re.compile(r'<span class="title">(.*?)</span>')
# 电影评分
findstar = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
# 评价人数
findnumeva =re.compile(r'<span>(\d*)人评价</span>')
# 电影评价
findeinq = re.compile(r'<span class="inq">(.*)</span>')
# 电影简介
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)
# 爬取网页
def getData(baseurl):
    datalist = []
    # 调用获取页面条数
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        # 调用geturl获取页面数据
        html = getURL(url)  # 变量存储返回值
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        # 查找符合要求的字符串组成列表
        for i in soup.find_all('div', class_="item"):
            data = []  # 存储一个电影所有信息
            item = str(i)
            link = re.findall(findlink,item)[0]
            data.append(link)
            # print(link) 链接
            img = re.findall(findImg,item)[0]
            data.append(img)
            # print(img)图片
            title = re.findall(findtitle,item)
            # print(title)名称
            if(len(title)==2):
                ctitle = title[0]
                data.append(ctitle)
                otitle = title[1].replace('/','')
                otitle = otitle.replace(u'\xa0','')
                data.append(otitle.strip())
            else:
                data.append(title[0])
                data.append(' ')
            # print(star)评分
            star = re.findall(findstar,item)[0]
            data.append(star)
            # print(numeva)评价人数
            numeva = re.findall(findnumeva,item)[0]
            data.append(numeva)
            inq = re.findall(findeinq,item)
            if len(inq)!=0:
                inq = inq[0].replace("。",'')
                data.append(inq)
            else:
                data.append(' ')

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?','',bd) # remove br换行
            bd = re.sub('/','',bd) # remove /
            bd = bd.replace(u'\xa0','')
            data.append(bd.strip())
            datalist.append(data)
            # print(data)
    return datalist



# 得到指定的一个网页的url
def getURL(url):
    # 用户代理
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0"
    }
    # 将请求封装为一个request对象
    request = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        # 通过open方法获取请求
        data = urllib.request.urlopen(request)
        html = data.read().decode("utf-8")
        # print(html)
    except Exception as e:
        print(e)
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "message"):
            print(e.message)
        if hasattr(e, "reason"):
            print(e.reason)
    return html




# 保存数据
def saveData(datalist,path):
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet("sheet1",cell_overwrite_ok=True)
    colum = ("电影详情链接","电影海报链接","电影名称","英文名","评分","评价人数","主旨","详情")
    for i in range(0,8):
        sheet.write(0,i,colum[i]) # 列名
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    book.save(path)
    print("存储完成！！！！")

if __name__ == '__main__':
    main()
