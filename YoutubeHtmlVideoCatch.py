#!/usr/bin/env python3
# coding=utf-8

# BeautifulSoup是第三方库，不过功能更强大，代码量更少。文档请参考
# http://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html

from bs4 import BeautifulSoup
import urllib.request
import os
import sys
from Youtube_video_db_operation import *
import ssl
# 设置 全局取消证书验证 http://blog.csdn.net/moonhillcity/article/details/52767999
ssl._create_default_https_context = ssl._create_unverified_context

default_save_video_path = '/Users/Vbon/Desktop/YoutubeDL/'
video_init_url = 'https://www.youtube.com/watch?v=Zbdjk_Bv4yg'

def downloadpage(url):

    fp = urllib.request.urlopen(url)
    data = fp.read()
    fp.close()

    # proxy_handler = urllib.request.ProxyHandler({'http': 'http://127.0.0.1:1087'})
    # opener = urllib.request.build_opener(proxy_handler)
    # r = opener.open(url)
    # data = r.read()
    # opener.close()

    # proxy_support = urllib.request.ProxyHandler({'http': 'localhost:1087'})
    # opener = urllib.request.build_opener(proxy_support)
    # urllib.request.install_opener(opener)
    # aa = urllib.request.urlopen(url)
    # data = aa.read()
    # print(data)

    return data


def parsehtml(data):
    soup = BeautifulSoup(data,'lxml')
    url_watch_list = []
    for x in soup.findAll('a'):
        a_href = x.attrs['href']
        if 'https://www.youtube.com/watch' in a_href:
            if a_href not in url_watch_list:
                url_watch_list.append(a_href)
        else:
            if '/watch' in a_href:
                full_href = 'https://www.youtube.com' + a_href
                if full_href not in url_watch_list:
                    url_watch_list.append(full_href)

    insert_success_count = 0
    for url_str in url_watch_list:
        if url_str == '':
            continue
        else:
            db_coperation = Youtube_db_operation()
            isExist = db_coperation.db_select_data_repeat(url_str)
            if isExist >= 1:
                print('数据库已存在:' + url_str + ',不插入此条数据')
            else:
                db_coperation.db_insert_data(url_str)
                insert_success_count += 1
    print('成功往数据库插入新数据：%d条' %(insert_success_count))


    db_coperation_2 = Youtube_db_operation()
    db_coperation_2.db_count_data_all() # 获取数据库总数据数量

    # time.sleep(5) # 休息一下，以免被封ip

    isContinue = True
    while(isContinue):
        unDownloadCount = db_coperation_2.db_count_unDownload_data_all()
        # 如果数据库中视频的未下载数量超过10条则暂停获取视频url爬虫
        if unDownloadCount < 10:
            isContinue = False
            # 循环执行
            parsehtml(downloadpage(db_coperation_2.db_select_data_isRelevanceSearch()))
        else:
            print('未下载的视频数量过多(>10),共有未下载视频%d个，暂停爬虫'%(unDownloadCount))

            video_url = db_coperation_2.db_select_data_unDownloaded()

            # ss_file_path = cur_file_dir() + '/You_dl_exc.sh'
            # exc = 'bash ' + ss_file_path
            exc = 'youtube-dl --proxy 127.0.0.1:1087 -o ' + default_save_video_path + '"%(title)s.%(ext)s" ' + video_url + ' --exec \'python3 /Users/Vbon/Documents/VideoPorter/update_video_download_status.py \'' + video_url + '\'\''
            print(os.system(exc))


            time.sleep(5)  # 休息一下



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
    parsehtml(downloadpage(video_init_url))
    # parsehtml("""
    # <a href="www.google.com"> google.com</a>
    # <A Href="www.pythonclub.org"> PythonClub </a>
    # <A HREF = "www.sina.com.cn"> Sina </a>
    # """)x.attrs['href']