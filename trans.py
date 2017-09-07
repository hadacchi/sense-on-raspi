# coding: utf-8

from dbhandler import dbhandler
from sqlite3handler import sqlite3handler
from conf import dbattr
from datetime import timedelta, datetime

# timezone
JST = timedelta(hours=9)

# DBへ接続
db  = dbhandler(dbattr)
sdb = sqlite3handler('data.db')

# read sensery data. ID is 1
data = [(1, (datetime.strptime(t,'%Y-%m-%d %H:%M:%S')+JST).strftime('%Y-%m-%d %H:%M:%S'), val, vol) for t, val, vol in sdb.select_data('light')]

# select
for subdata in zip(*[iter(data)]*100):
    db.insert_data('light', subdata)

