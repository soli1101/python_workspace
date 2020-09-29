import time
print(time.ctime())

print('-------------------------')
print(time.gmtime(), type(time.gmtime()))
print('-------------------------')
print(time.gmtime().tm_mon)
print(time.gmtime().tm_mday)