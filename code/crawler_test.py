from urllib import response
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配`
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt

# import sqlite3  # 进行SQLite数据库操作

# 正则提取
findlink = re.compile(r'<a href="(.*?)">')
findpic = re.compile(r'<img.*src"(.*?)"', re.S)
findtitle = re.compile(r'<span class="title">(.*)</span>')
findbd = re.compile(r'<p class="">.*</p>', re.S)


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    Savepath = "doubanTop250.xls"
    SaveData(datalist, Savepath)


def getData(baseurl):
    Datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = URL(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            item = str(item)
            data = []
            Link = re.findall(findlink, item)[0]
            data.append(Link)
            pic = re.findall(findpic, item)[0]
            data.append(pic)
            title = re.findall(findtitle, item)
            if len(title) == 2:
                ctitle = title[0]
                data.append(ctitle)
                otitle = title[1]
                data.append(otitle)
            else:
                ctitle = title[0]
                otitle = ""
            data.append(ctitle)
            data.append(otitle)
            bd = re.findall(findbd, item)
            data.append(bd)
            Datalist.append(data)
    return Datalist


def SaveData(Datalist, Savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet("douban250", cell_overwrite_ok=True)
    col = ("链接", "图片", "中文标题", "外文标题", "阵容")
    for i in range(0, 5):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        data = Datalist[i]
        print('第%d条' % (i + 1))
        for j in range(0, 5):
            sheet.write(i + 1, j, data[j])
    book.save(Savepath)


def URL(url):
    head = {
        "User-Agent":
        "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    req = urllib.request.Request(url, headers=head)
    responser = urllib.request.urlopen(req)
    html = ""
    html = responser.read().decode("utf-8")
    return html


if __name__ == "__main__":
    main()
    print("爬取完成")
