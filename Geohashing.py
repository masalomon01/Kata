# 5kyu
from datetime import datetime
import hashlib

def geohash(dow, date=datetime.utcnow()):
    s = str(date)[:10] + "-" + str("%.2f" % dow)
    m = hashlib.md5(s.encode('utf-8')).hexdigest()
    m1, m2 = float.fromhex('0.' + m[:16]), float.fromhex('0.' + m[-16:])
    return [round(m1, 6), round(m2, 6)]


print geohash(10458.68, datetime(2005,5,26))# , [0.857713, 0.544543]);
print geohash(10458.68)# , [0.857713, 0.544543]);
print geohash(10458)
