#!/usr/bin/env python


from yahoo_finance import Share
import pymysql.cursors


def get(symbol, start, end):
  share = Share(symbol)
  return share.get_historical(start, end)


def yahoo2db(share):
  d = [] 
  d.append(share['Symbol'])
  d.append(share['Date'])
  """
  d.append(float(share['Open']))
  d.append(float(share['Close']))
  d.append(float(share['High']))
  d.append(float(share['Low']))
  d.append(int(share['Volume']))
  d.append(float(share['Adj_Close']))

  """
  d.append(share['Open'])
  d.append(share['Close'])
  d.append(share['High'])
  d.append(share['Low'])
  d.append(share['Volume'])
  d.append(share['Adj_Close'])


  return tuple(d) 

if __name__ == '__main__':
  connection = pymysql.connect(host="192.168.1.80",
                               user="gaoxinbo",
                               db="stock",
                               password="840326")
  sql = "replace into historical_data (symbol, date, open, close, high, low, volume, adj_close) values (%s,     %s,   %s,   %s,    %s,   %s,  %s,     %s) "
  q = get("BABA", "2017-01-01", "2017-04-30")
  
  l = []
  for item in q:
    db = yahoo2db(item)
    l.append(db)
    
  with connection.cursor() as cursor:
    cursor.executemany(sql, l)
    connection.commit()
 
