# coding: utf-8

from conf import dbattr,PID
from datetime import timedelta, datetime
import os
import sys

class PidFileHandler:
    def __init__(self, pidFile):
        '開始時'
        #sys.stderr.write('init\n')
        #sys.stderr.flush()
        self.pidFile = pidFile
        self.storepid()

    def __enter__(self):
        'withステートメントで呼ばれた時のみ'
        #sys.stderr.write('enter\n')
        #sys.stderr.flush()
        pass

    def storepid(self):
        'PIDファイルを生成'
        self.pid = os.getpid()
        if os.path.isfile(self.pidFile):
            raise Exception('already started')
        with open(self.pidFile, 'w') as f:
            f.write(str(self.pid))

    def deletepid(self):
        'PIDファイルを削除'
        # このオブジェクトが破棄される時に呼ばれる＝pidのプロセスは死ぬ直前
        if os.path.isfile(self.pidFile):
            os.remove(self.pidFile)

    def __del__(self):
        '破棄時'
        s#ys.stderr.write('del\n')
        s#ys.stderr.flush()
        self.deletepid()

    def __exit__(self, typ, val, tra):
        'withステートメントを抜ける時のみ'
        s#ys.stderr.write('exit\n')
        s#ys.stderr.flush()
        self.deletepid()
