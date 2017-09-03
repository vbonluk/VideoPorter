import pymysql.cursors
import sys


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
            sql = "UPDATE Youtube_video SET isDownloaded = '1' WHERE Youtube_video_url = '%s' "
            data = (url)
            isSuccess = cursor.execute(sql % data)
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