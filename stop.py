# coding: utf-8

import os
import signal
from conf import PID

if os.path.isfile(PID):
    with open(PID,'r') as f:
        pid = int(f.read())
    os.kill(pid, signal.SIGUSR1)
else:
    raise Exception('no run.pid file')
