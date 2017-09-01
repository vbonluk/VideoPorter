#!/usr/bin/env python  
# coding=utf-8

# BeautifulSoup是第三方库，不过功能更强大，代码量更少。文档请参考
# http://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html

from bs4 import BeautifulSoup
import urllib.request
import os
import ssl
# 设置 全局取消证书验证 http://blog.csdn.net/moonhillcity/article/details/52767999
ssl._create_default_https_context = ssl._create_unverified_context

def downloadpage(url):
    fp = urllib.request.urlopen(url)
    data = fp.read()
    fp.close()
    return data


def parsehtml(data):
    # soup = BeautifulSoup(data,'lxml')
    # url_watch_list = []
    # for x in soup.findAll('a'):
    #     a_href = x.attrs['href']
    #     if 'https://www.youtube.com/watch' in a_href:
    #         url_watch_list.append(a_href)
    #     else:
    #         if '/watch' in a_href:
    #             url_watch_list.append('https://www.youtube.com' + a_href)
    #
    #
    # print(url_watch_list)

    os.system('cd /Users/Vbon/Desktop/YoutubeDL')
    print(os.system('youtube-dl https://www.youtube.com/watch\?v\=Zbdjk_Bv4yg'))



if __name__ == "__main__":
    parsehtml(downloadpage('https://www.youtube.com/watch?v=Zbdjk_Bv4yg'))
    # parsehtml("""
    # <a href="www.google.com"> google.com</a>
    # <A Href="www.pythonclub.org"> PythonClub </a>
    # <A HREF = "www.sina.com.cn"> Sina </a>
    # """)x.attrs['href']