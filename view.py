# coding: utf-8

import datetime
import dbhandler
import pandas

db   = dbhandler.dbhandler('data.db')
data = db.select_data('light', 'order by deal_date',None)
t    = [datetime.datetime.strptime(d[0],'%Y-%m-%d %H:%M:%S') for d in data]
val  = [d[1:] for d in data]
df   = pandas.DataFrame(data=val, index=t, columns=['val','voltage'])
print(df)
#print(t)
#print(data[:10])
#print(data[:10])
