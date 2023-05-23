import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent


# 请求数据
def get_data():
    url = 'https://book.douban.com/latest'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35'}
    data = requests.get(url, headers=headers)
    # print(data.text)
    return data


# 解析数据
def parse_data(data):
    soup = BeautifulSoup(data.text, features="html.parser")
    # print(soup)
    book_list = soup.find('ul', {'class': 'chart-dashed-list'})
    book_list = book_list.find_all('li')
    books = list(book_list)
    # print(books[0])

    img_urls = []
    titles = []
    ratings = []
    authors = []
    prices = []
    for book in books:
        # 获取图片地址
        img_url = book.find_all('a')[0].find('img').get('src')
        img_urls.append(img_url)
        # 获取图书标题
        title = book.find_all('a')[1].get_text()
        titles.append(title)
        # 获取出版社信息
        author = book.find_all('p', {'class': 'subject-abstract color-gray'})[0].get_text()
        author = author.replace('\n', '').replace(' ', '')
        authors.append(author)
        # 获取评分
        rating = book.find_all('p')[1].find('span', {'class': 'font-small color-red fleft'}).get_text()
        rating = rating.replace('\n', '').replace(' ', '')
        ratings.append(rating)
        # 获取价格
        price = book.find_all('a')[2].get_text()
        price = price.replace('\n', '').replace(' ', '')
        prices.append(price)
    # print('img_urls:',img_urls)
    # print('titles:',titles)
    # print('authors:',authors)
    # print('ratings:',ratings)
    # print('prices:',prices)
    return img_urls, titles, authors, ratings, prices


# 存储数据
def save_data(img_urls, titles, authors, ratings, prices):
    result = pd.DataFrame()
    result['img_urls'] = img_urls
    result['titles'] = titles
    result['authors'] = authors
    result['ratings'] = ratings
    result['prices'] = prices
    result.to_csv('result.csv', index=None)


# 开始爬取
def run():
    data = get_data()
    img_urls, titles, authors, ratings, prices = parse_data(data)
    save_data(img_urls, titles, authors, ratings, prices)


if __name__ == '__main__':
    run()