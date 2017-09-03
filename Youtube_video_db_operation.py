#!/usr/bin/env python
# coding=utf-8

import pymysql.cursors
import time

class Youtube_db_operation:

    def __init__(self):
        pass

    def connDB(self):
        # 连接数据库
        connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='root',
            db='Youtube_Porter_db',
            charset='utf8'
        )
        return connect


    def db_insert_data(self,url='',name=''):
        if url == '':
            print('url is empty , insert failure')
            return
        else:
            connect = self.connDB()
            # 获取游标
            cursor = connect.cursor()

            # 插入数据
            sql = "INSERT INTO Youtube_video_mark (Youtube_video_name,Youtube_video_url, isDownloaded, isUploaded, size, time, timeStr, isUnavailable, downloadTime, downloadTimeStr, uploadTime, uploadTimeStr, searchTime, searchTimeStr) VALUES ( '%s', '%s', %d, %d, %d, %d, '%s', %d, %d, '%s', %d, '%s', %d, '%s')"
            system_time_format = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            data = (name, url, 0, 0, 0, 0, '0', 0, 0, '0', 0, '0', time.time(), system_time_format)
            sql_full = sql % data
            cursor.execute(sql_full)
            connect.commit()

            # 关闭连接
            cursor.close()
            connect.close()
            # print('成功插入', cursor.rowcount, '条数据')

    def db_update_data(self):
        print()

    def db_select_data_repeat(self,url=''):
        if url == '':
            print('url is empty , select failure')
            return
        else:
            connect = self.connDB()
            # 获取游标
            cursor = connect.cursor()

            # 查询数据
            sql = "SELECT id FROM Youtube_video_mark WHERE Youtube_video_url = '%s' "
            data = (url)
            cursor.execute(sql % data)
            url_list = []
            for row in cursor.fetchall():
                # print(row)
                url_list.append(row)

            # 关闭连接
            cursor.close()
            connect.close()

            if len(url_list) > 0:
                return 1
            else:
                return 0

    def db_update_data_Relevance(self, url=''):
        if url == '':
            print('url is empty , update failure')
            return
        else:
            connect = self.connDB()
            # 获取游标
            cursor = connect.cursor()

            # 修改数据
            sql = "UPDATE Youtube_video_mark SET isUnavailable = 1 WHERE Youtube_video_url = '%s' "
            data = (url)
            isSuccess = cursor.execute(sql % data)
            connect.commit()
            if isSuccess == 1:
                print('成功将1条数据' + url + '标识为已经关联搜索过 isUnavailable = 1')

            # 关闭连接
            cursor.close()
            connect.close()

    def db_select_data_isRelevanceSearch(self):

        connect = self.connDB()
        # 获取游标
        cursor = connect.cursor()

        # 查询数据
        sql = "SELECT Youtube_video_url FROM Youtube_video_mark WHERE isUnavailable = 0"
        cursor.execute(sql)
        Youtube_video_url = cursor.fetchone()[0]

        # 关闭连接
        cursor.close()
        connect.close()

        self.db_update_data_Relevance(Youtube_video_url)

        return Youtube_video_url

    def db_select_data_unDownloaded(self):

        connect = self.connDB()
        # 获取游标
        cursor = connect.cursor()

        # 查询数据
        sql = "SELECT Youtube_video_url FROM Youtube_video_mark WHERE isDownloaded = 0"
        cursor.execute(sql)
        Youtube_video_url = cursor.fetchone()[0]

        # 关闭连接
        cursor.close()
        connect.close()

        return Youtube_video_url

    def db_select_data_all(self):
        print()

    def db_count_data_all(self):

        connect = self.connDB()
        # 获取游标
        cursor = connect.cursor()

        # 查询数据
        sql = "SELECT COUNT(*) FROM Youtube_video_mark"
        cursor.execute(sql)
        Count_url = cursor.fetchone()[0]

        print('当前数据总数：%s条'%(Count_url))

        # 关闭连接
        cursor.close()
        connect.close()

        return Count_url

    def db_count_unDownload_data_all(self):

        connect = self.connDB()
        # 获取游标
        cursor = connect.cursor()

        # 查询数据
        sql = "SELECT COUNT(*) FROM Youtube_video_mark WHERE isDownloaded = 0"
        cursor.execute(sql)
        Count_url = cursor.fetchone()[0]

        print('当前数据总数：%s条' % (Count_url))

        # 关闭连接
        cursor.close()
        connect.close()

        return Count_url
