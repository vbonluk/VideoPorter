#!/usr/bin/env python
# coding=utf-8

import pymysql.cursors
import time

'''
  数据库Youtube_video表
  `id` int(4) unsigned NOT NULL AUTO_INCREMENT,
  `Youtube_video_url` varchar(255) NOT NULL COMMENT 'Youtube_video_url',
  `isDownloaded` INT NOT NULL COMMENT DEFAULT 0 '是否下载过',
  `isUploaded` INT NOT NULL DEFAULT 0 COMMENT '是否上传过',
  `duration` DOUBLE NOT NULL DEFAULT '0.00' COMMENT '是否在下载',
  `isUnavailable` INT NOT NULL DEFAULT 0 COMMENT '是否不可用',
  `time` varchar(255) NOT NULL DEFAULT '0' COMMENT '生成此条数据的时间',
  `time_str` varchar(255) NOT NULL DEFAULT '0' COMMENT '生成此条数据的时间',
'''


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


    def db_insert_data(self,url=''):
        if url == '':
            print('url is empty , insert failure')
            return
        else:
            connect = self.connDB()
            # 获取游标
            cursor = connect.cursor()

            # 插入数据
            sql = "INSERT INTO Youtube_video (Youtube_video_url, isDownloaded, isUploaded, time, time_str) VALUES ( '%s', '%d', %d , '%s','%s')"
            system_time = time.time()
            system_time_format = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            data = (url, 0, 0, system_time, system_time_format)
            cursor.execute(sql % data)
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
            sql = "SELECT id FROM Youtube_video WHERE Youtube_video_url = '%s' "
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
            sql = "UPDATE Youtube_video SET isUnavailable = '1' WHERE Youtube_video_url = '%s' "
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
        sql = "SELECT Youtube_video_url FROM Youtube_video WHERE isUnavailable = '0'"
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
        sql = "SELECT Youtube_video_url FROM Youtube_video WHERE isDownloaded = '0'"
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
        sql = "SELECT COUNT(*) FROM Youtube_video"
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
        sql = "SELECT COUNT(*) FROM Youtube_video WHERE isDownloaded = '0'"
        cursor.execute(sql)
        Count_url = cursor.fetchone()[0]

        print('当前数据总数：%s条' % (Count_url))

        # 关闭连接
        cursor.close()
        connect.close()

        return Count_url
