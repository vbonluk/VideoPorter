#!/usr/bin/env python  
# coding=utf-8

# BeautifulSoup是第三方库，不过功能更强大，代码量更少。文档请参考
# http://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html

from bs4 import BeautifulSoup
import urllib.request
import os
import sys
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
    ss_file_path = cur_file_dir() + '/You_dl_exc.sh'
    exc = 'bash ' + ss_file_path
    print(os.system(exc))


#获取脚本文件的当前路径
def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

if __name__ == "__main__":
    parsehtml(downloadpage('https://www.youtube.com/watch?v=Zbdjk_Bv4yg'))
    # parsehtml("""
    # <a href="www.google.com"> google.com</a>
    # <A Href="www.pythonclub.org"> PythonClub </a>
    # <A HREF = "www.sina.com.cn"> Sina </a>
    # """)x.attrs['href']