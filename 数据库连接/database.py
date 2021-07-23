import pymysql
from pymysql.cursors import DictCursor


def main():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='a', charset='utf8',
                           cursorclass=DictCursor)
    with conn.cursor() as cursor:
        cursor.execute('select * from b')
        # result = cursor.execute('insert into b values (5,5,"韩七",null,null)')
        # result=cursor.execute('delete from b where id=%s',(no, ))
        result = cursor.fetchall()
        # conn.close()
        for row in result:
            print(row['id'], end='\t')
            print(row['user_name'])


if __name__ == '__main__':
    main()

print("okok %d岁" % (17))

print("我叫{}今年{}岁".format("zs",17))
