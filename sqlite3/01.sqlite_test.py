import sqlite3

print(sqlite3.version)

conn=sqlite3.connect('sqlite3/example.db')

c=conn.cursor()

c.execute('''
            create table if not exists stocks(
                date text, 
                trans text,
                symbol text,
                qty real,
                price real
            )
        ''')

c.execute('''
            insert into stocks(date,trans,symbol,qty,price) 
                        values('19-07-13','BUY','RHAT',100,35.14)
        ''')
conn.commit()
conn.close()
