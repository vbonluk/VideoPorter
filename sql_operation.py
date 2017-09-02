#!/usr/bin/env python
# coding=utf-8

import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='Youtube_Porter_db',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()

'''
  数据库Youtube_video表
  `id` int(4) unsigned NOT NULL AUTO_INCREMENT,
  `Youtube_video_url` varchar(255) NOT NULL COMMENT 'Youtube_video_url',
  `isDownloaded` INT NOT NULL COMMENT '是否下载过',
  `isUploaded` INT NOT NULL DEFAULT '0.00' COMMENT '是否上传过',
  `duration` DOUBLE NOT NULL DEFAULT '0.00' COMMENT '时长',
  `isUnavailable` INT NOT NULL DEFAULT '0.00' COMMENT '是否不可用',
'''

# 插入数据
sql = "INSERT INTO Youtube_video (Youtube_video_url, isDownloaded, isUploaded) VALUES ( '%s', '%d', %d )"
data = ('https://www.youtube.com/watch?v=Zbdjk_Bv4yg', 0, 0)
cursor.execute(sql % data)
connect.commit()
print('成功插入', cursor.rowcount, '条数据')

# 修改数据
sql = "UPDATE trade SET saving = %.2f WHERE account = '%s' "
data = (8888, '13512345678')
cursor.execute(sql % data)
connect.commit()
print('成功修改', cursor.rowcount, '条数据')

# 查询数据
sql = "SELECT name,saving FROM trade WHERE account = '%s' "
data = ('13512345678',)
cursor.execute(sql % data)
for row in cursor.fetchall():
    print("Name:%s\tSaving:%.2f" % row)
print('共查找出', cursor.rowcount, '条数据')

# 删除数据
sql = "DELETE FROM trade WHERE account = '%s' LIMIT %d"
data = ('13512345678', 1)
cursor.execute(sql % data)
connect.commit()
print('成功删除', cursor.rowcount, '条数据')


# 关闭连接
cursor.close()
connect.close()