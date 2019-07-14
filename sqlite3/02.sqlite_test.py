import sqlite3,csv

conn=sqlite3.connect('sqlite3/example.db')
c=conn.cursor()

'''
symbol='RHAT'
c.execute("select * from stocks where symbol='%s'"%symbol)

items = c.fetchall()

for item in items:
    print(item)

t=('RHAT',)
sql='select * from stocks where symbol=?'
c.execute(sql,t)
print(c.fetchall())
'''

purchases = [('06-03-28', 'BUY', 'IBM', 1000, 45.00),
            ('06-05-28', 'BUY', 'MSFT', 1000, 72.00),
            ('06-05-30', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('insert into stocks values(?,?,?,?,?)',purchases)
conn.commit()

c.execute('select * from stocks order by price')
rows=c.fetchall()
for row in rows:
    print(row)

for row in c.execute('select * from stocks order by price'):
    print(row)

c.close