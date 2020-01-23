import requests
from bs4 import BeautifulSoup
import pymysql
import turtle
mainURL = 'http://forecast.weather.com.cn/town/weather1dn/101161107002.shtml'
req = requests.get(url = mainURL)
req.encoding = 'utf-8'
html = req.text
html1 = BeautifulSoup(html,'lxml')
html2 = html1.find('div', class_='todayModel weatherBg01')
db = pymysql.connect(host='127.0.0.1', user='root', password='root', db='asd', port=3306, charset='utf8')
cursor = db.cursor()
zhcn = """alter table red convert to character set utf8;"""
cursor.execute(zhcn)
def get_source(html):
    html1 = BeautifulSoup(html, 'lxml')
    soup = html1.find('div', class_='todayModel weatherBg01')
    Temp(soup)
    weather(soup)
    maxTemp(soup)
    minTemp(soup)
    #warning(soup)
    wind(soup)
    limit_line(soup)
    weatherALL(soup)
def Temp(soup):
    list = soup.find('div', class_='tempDiv')
    content = list.text.replace("\n", "")
    print('实时温度：'+content)
    return content
def weather(soup):
    list = soup.find('div', class_='weather dis')
    content = list.text.replace("\n", "")
    print('天气：'+content)
    return content
def maxTemp(soup):
    list = soup.find('div', id='maxTempDiv')
    content = list.text
    print('最高温度'+content)
    return content
def minTemp(soup):
    list = soup.find('div', id='minTempDiv')
    content = list.text
    print('最低温度'+content)
    return content
def warning(soup):
    list = soup.find('div', id='yujing')
    content = list.text.replace("\n", "")
    print(content)
    return content
def wind(soup):
    list = soup.find('p')
    content = list.text.replace("\n", "")
    print(content)
    return content
def limit_line(soup):
    list = soup.find('p', class_='dis')
    content = list.text.replace("\n", "")
    print(content)
    return content
def weatherALL(soup):
    list = soup.find('ul', id='weatherALL').find_all('li')
    for soup in list:
        time = soup.find('div', class_='time').text.replace("\n", "")
        weather = soup.find('i').get('title')
        wind = soup.find('div', class_='wind').text.replace("\n", "")
        windL = soup.find('div', class_='windL').text.replace("\n", "")
        content = '{},天气：{},风向：{},风力：{}'
        content1 = content.format((time),(weather),(wind),(windL))
        print(content1)
        return content1
if __name__ == '__main__':
    get_source(html)