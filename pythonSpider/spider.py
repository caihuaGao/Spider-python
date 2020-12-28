# -*- coding = utf-8 -*-
# @Time: 2020/12/23 14:23
# @Author: 高才华
# @File: spider.py
# @Software: PyCharm

import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup
import re
import xlwt
import sqlite3

# 影片的链接
movieLink = re.compile(r'<a href="(.*?)">')
# 影片的图片
imgLink = re.compile(r'<img.*src="(.*?)"',re.S) # re.S 忽略换行符 因为.不包括换行符
# 影片的片名
movieName = re.compile(r'<span class="title">(.*)</span>')
# 影片的评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 影片的评价
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 影片概况
findInfo = re.compile(r'<span class="inq">(.*)</span>')
# 影片相关内容
findbd = re.compile(r'<p class="">(.*?)</p>',re.S)

def main(saveType):
    baseUrl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseUrl)
    savepath = ".\\豆瓣电影Top250.xls"
    dbpath = "movie.db"
    # 3.保存数据
    if saveType == "db":
        saveDataToDb(datalist,dbpath)
    else:
        saveDataToXls(datalist,savepath)
# 1.爬取网页
def getData(baseUrl):
    dataList = []
    for i in range(0,10):
        url = baseUrl + str(i*25)
        html = askUrl(url)
        print(url)
        # 2.逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"):
            data = []
            item = str(item)

            titles = re.findall(movieName,item)
            if len(titles) == 2:
                cName = titles[0]
                data.append(cName)
                oName = titles[1].replace("/","")
                oName = oName.replace(" ","").strip()
                data.append(oName)
                print(oName)
            else:
                data.append(titles[0])
                data.append(" ")  # 留空站位

            link = re.findall(movieLink,item)[0]
            data.append(link)

            imgStc = re.findall(imgLink,item)[0]
            data.append(imgStc)

            rating = re.findall(findRating,item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)

            inq = re.findall(findInfo,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findbd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?',"",bd)
            data.append(bd.strip())
            dataList.append(data) #一部电影的处理
    return dataList
# 3.保存数据
def saveDataToXls(datalist,savepath):
    print(savepath)
    print(len(datalist))
    workbook = xlwt.Workbook(encoding="utf-8",style_compression=0) # 压缩效果
    worksheet = workbook.add_sheet("豆瓣电影Top250",cell_overwrite_ok=True) #覆盖
    col =("影片中文名","影片外文名","电影详情链接","电影图片链接","评分","评价人数","概况","相关信息")
    for i in range(0, len(col)):
        worksheet.write(0,i,col[i])
    for i in range(0, len(datalist)):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0, len(data)):
            worksheet.write(i+1,j,data[j])
    workbook.save(savepath)

def saveDataToDb(datalist,dbpath):
    print(dbpath)
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
        sql = '''
            insert into movie250(cname,ename,info_link,pic_link,score,rated,intrduction,info)
            values (%s)
        '''%",".join(data)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()



def init_db(dbpath):
    conn = sqlite3.connect(dbpath) # 打开或创建数据库文件
    print("成功打开了数据库")
    c = conn.cursor() #获取游标
    sql = '''
        create table movie250
            (id integer primary key autoincrement,
            cname varchar ,
            ename varchar ,
            info_link text ,
            pic_link text ,
            score numeric ,
            rated numeric ,
            intrduction text ,
            info text
            );
    '''
    c.execute(sql) # 执行sql语句
    conn.commit()
    conn.close()

def askUrl(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"
    }
    req = urllib.request.Request(url=url, headers=headers)
    try:
        unverifed = ssl._create_unverified_context()  # 避开证书验证
        respones = urllib.request.urlopen(req,context=unverifed)
        return respones.read().decode('utf-8')
    except Exception as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

main("db")