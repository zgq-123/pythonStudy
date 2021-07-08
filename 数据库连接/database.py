import pymysql


def main():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='a', charset='utf8')
    with conn.cursor() as cursor:
        cursor.execute('select * from b')
        # result = cursor.execute('insert into b values (5,5,"韩七",null,null)')
        # result=cursor.execute('delete from b where id=%s',(no, ))
        result = cursor.fetchall()
        for row in result:
            print(row[2])


if __name__ == '__main__':
    main()
