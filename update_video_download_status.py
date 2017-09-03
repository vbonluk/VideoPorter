import pymysql.cursors
import sys
import time


def connDB():
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

def update(url=''):
    if url == '':
        print('')
    else:
        connect = connDB()
        # 获取游标
        cursor = connect.cursor()

        # 查询数据
        sql_select = "SELECT COUNT(*) FROM Youtube_video WHERE Youtube_video_url = '%s'"
        cursor.execute(sql_select % url)
        Count_url = cursor.fetchone()[0]
        if Count_url > 0:
            # 修改数据
            sql = "UPDATE Youtube_video_mark SET isDownloaded = 1,downloadTime = %d,downloadTimeStr = '%s' WHERE Youtube_video_url = '%s' "
            system_time_format = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            data = (time.time(),system_time_format,url)
            sql_full = sql % data
            isSuccess = cursor.execute(sql_full)
            connect.commit()
            if isSuccess == 1:
                print('成功下载1条数据' + url + ' isDownloaded = 1')

        # 关闭连接
        cursor.close()
        connect.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        param_1 = sys.argv[1]
        # print(param_1)
        update(param_1)