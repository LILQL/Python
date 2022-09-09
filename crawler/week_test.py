import urllib.request, urllib.error
import xlwt
import re
from bs4 import BeautifulSoup

#正则提取规则
findLink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'<img.*src="(.*?)">', re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(
    r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getdata_1(baseurl)
    savepath = "douban250.xls"
    saveData_1(datalist, savepath)


def getdata_1(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL_1(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)
            link = re.findall(findLink, item)[0]  # 通过正则表达式查找
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle, item)
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")  #消除转义字符
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', "", bd)
            bd = re.sub('/', "", bd)
            data.append(bd.strip())
            datalist.append(data)

    return datalist


def askURL_1(url):
    head = {
        "User-Agent":
        "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    request_1 = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response_1 = urllib.request.urlopen(request_1)
        html = response_1.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


def saveData_1(datalist, savepath):
    print("save......")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('douban250', cell_overwrite_ok=1)
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)


if __name__ == "__main__":
    main()
    print("爬取完成！")