import pymysql

def conn_db():
    conn = pymysql.connect(host='localhost',
                            user='root',
                            password='qwer1234',
                            db='test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    return conn

def create_table():
    conn=conn_db()
    cursor=conn.cursor()
    cursor.execute('''create table if not exists users(
                    userid varchar(11) NOT NULL,
                    email varchar(255) NOT NULL,
                    adress varchar(255),
                    password varchar(255) NOT NULL,
                    PRIMARY KEY (userid)
                    )''')
    conn.commit
    conn.close