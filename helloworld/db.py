import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', database='flask_shopping')


def get_all_goods():
    sql = 'SELECT * FROM goods'
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()

    return result
