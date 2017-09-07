# coding: utf-8

import sqlite3

__version__ = '0.2.0'
__author__  = 'hadacchi'

class sqlite3handler(object):
    def __init__(self, fname):
        self.con = None
        self.cur = None
        self.db  = fname

    def connect(self, fname):
        self.con = sqlite3.connect(fname)
        self.cur = self.con.cursor()

    def connected(self):
        if self.con is None:
            return False
        return True

    def __del__(self):
        self.con.close()

    def insert_data(self, table, data):
        if not self.connected():
            self.connect(self.db)
        self.cur.executemany('insert into '+table+' values (?,?,?)', data)
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

