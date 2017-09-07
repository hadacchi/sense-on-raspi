# coding: utf-8

import dbhandler

db=dbhandler.dbhandler('data.db')
db.connect('data.db')
db.cur.execute('drop table if exists light')
db.cur.execute('create table light (t datetime, val real, voltage real)')
db.con.commit()
del(db)
