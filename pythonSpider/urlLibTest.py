# -*- coding = utf-8 -*-
# @Time: 2020/12/22 13:24
# @Author: 高才华
# @File: urlLibTest.py
# @Software: PyCharm

import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup
import re
# get
# respones = urllib.request.urlopen("http://www.baidu.com")
# print(respones.read().decode('utf-8'))

# post
# data = bytes(urllib.parse.urlencode({"hello":"world"},encoding="utf-8"))
# respones = urllib.request.urlopen("http://httpbin.org/get",timeout=15)
# print(respones.read().decode('utf-8'))


url = "https://movie.douban.com/explore#!type=movie&tag=%E5%8A%A8%E7%94%BB&sort=rank&page_limit=20&page_start=20"
unverifed = ssl._create_unverified_context() # 避开证书验证
def askUrl(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"
    }
    req = urllib.request.Request(url=url, headers=headers)
    try:
        respones = urllib.request.urlopen(req,context=unverifed)
        return respones.read().decode('utf-8')
    except Exception as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

html = askUrl(url)
print("网页开始%s"%html)
# bs = BeautifulSoup(html,"html.parser")
# print(bs.title.string)
# print(bs.p.attrs)
# print(type(bs))
# print(bs.head.contents[-3])

import re
# t_list = bs.find_all(re.compile("a"))
# print(t_list)

# k_list = bs.find_all(class_="rating_num")
# print(k_list)

# t_list = bs.find_all(text=re.compile("\d"))
# print(t_list)

# t_list = bs.find_all("a",limit=3)
# print(t_list)

# 选择器
# t_list = bs.select("p") # 标签选择
# t_list = bs.select(".rating_num") # 通过类名查找
# t_list = bs.select("#id") # 通过id查找
# t_list = bs.select("p[calss='rating_num']") # 通过属性查找
# t_list = bs.select("div > p") # 通过子标签查找
# t_list = bs.select("header ~ div") # 通过兄弟标签
# print(t_list)


# 正则表达式
'''
. 表示任何单个字符
[ ] 表示字符集 对单个字符给出取值范围         [abc] 表示a,b,c [a-z]表示a到z单个字符
[^ ] 非字符集，对单个字符给出排除范围         [^abc] 表示非a或者b或者c的单个字符
* 表示前一个字符0次货无限次扩展              abc* 表示 ab, abc ,abcc,abccc 等
+ 表示前一个字符1次或无限次数扩展            abc+ 表示 abc , abcc, abccc 等
? 表示前一个字符0次或1次扩展                abc？ 表示 ab,abc
| 左右表达式任意一个                       abc|def 表示 abc,def

{m} 扩展前一个字符m次                      abc{2}d 表示 abccd
{m,n} 扩展前一个字符m到n次(包含m,n)          ab{1,2}c 表示 abc abbc
^ 匹配字符串开头                           ^abc表示abc在一个字符串的开头
$ 匹配字符串的结尾                          abc$表示ABC自一个字符串的结尾
() 分组标记，内部只能使用|操作符              (abc)表示abc,(abc|def)表示abc,def
\d  数组                                  等价于[0-9]
\w  单个字符                               等价于[A-Za-z0-9_]
'''
pat = re.compile("AA")
n = pat.search("CBAaAAAd")
print(n)

