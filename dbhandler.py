# coding: utf-8

import pymysql.cursors

__version__ = '0.3.0'
__author__  = 'hadacchi'

class dbhandler(object):
    def __init__(self, dbattr):
        self.con = None
        self.cur = None
        self.db  = dbattr

    def connect(self, dbattr):
        self.con = pymysql.connect(**dbattr)
        self.cur = self.con.cursor()

    def connected(self):
        if self.con is None:
            return False
        return True

    def __del__(self):
        if self.con is not None:
            self.con.close()

    def insert_data(self, table, data):
        if not self.connected():
            self.connect(self.db)
        size = len(data[0])
        fmt  = 'insert into '+table+' values ('+','.join(['%s']*size)+')'
        self.cur.executemany(fmt, data)
        self.con.commit()

    def select_data(self, table, optionstr='', optionparam=None):
        if not self.connected():
            self.connect(self.db)
        if optionparam is None:
            self.cur.execute('select * from '+table)
            return self.cur.fetchall()
        else:
            self.cur.execute('select * from '+table+ optionstr, optionparam)
            return self.cur.fetchall()

    def select_data_by_date(self, date):
        return self.select_data(' where deal_date=?', (date,))

