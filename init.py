# coding: utf-8

import sqlite3handler

db=sqlite3handler.sqlite3handler('data.db')
db.connect('data.db')
db.cur.execute('drop table if exists light')
db.cur.execute('create table light (t datetime, val real, voltage real)')
db.con.commit()
del(db)
