import pymysql

def adduser():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', charset='utf8')
    cursor = conn.cursor()
    conn.commit()
    cursor.execute('use userinfo')
    username="555"
    password="555"
    sql = "insert into user (`username`, `password`)values('" + str(username) + "','" + str(password) + "');"
    print(sql)

    count = cursor.execute(sql)
    print(count)
    conn.commit()
    cursor.close()
    conn.close()
    return "success"


if __name__ == '__main__':
    adduser()