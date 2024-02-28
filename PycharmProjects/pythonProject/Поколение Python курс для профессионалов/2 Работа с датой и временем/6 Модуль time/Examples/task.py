import time
import timeit
import datetime
import calendar
print(time.gmtime(0))
t = time.localtime()
print('Итак, на дворе {}-й год.'.format(t.tm_year))
print(t.tm_zone)
print(t.tm_isdst)
print(t.tm_gmtoff)


print(time.ctime(time.time()))
print(time.asctime())
print(time.asctime(time.gmtime()))
print(time.ctime())
print()

print(time.strftime('%d.%m.%Y', time.localtime()))