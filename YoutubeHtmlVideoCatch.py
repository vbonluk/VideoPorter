#!/usr/bin/env python  
# coding=utf-8

# BeautifulSoup是第三方库，不过功能更强大，代码量更少。文档请参考
# http://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html

from bs4 import BeautifulSoup
import urllib.request


def downloadpage(url):
    fp = urllib.request.urlopen(url)
    data = fp.read()
    fp.close()
    return data


def parsehtml(data):
    soup = BeautifulSoup(''.join(data))
    for x in soup.findAll('a'):
        print
        x.attrs['href']


if __name__ == "__main__":
    parsehtml(downloadpage('http://www.baidu.com'))
    # parsehtml("""
    # <a href="www.google.com"> google.com</a>
    # <A Href="www.pythonclub.org"> PythonClub </a>
    # <A HREF = "www.sina.com.cn"> Sina </a>
    # """)