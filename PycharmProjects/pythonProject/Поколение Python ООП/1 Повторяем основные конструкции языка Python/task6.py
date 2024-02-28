import sys

result = [tup.strip('()\n').split(',') for tup in sys.stdin]
for i in result:
    if float(i[0]) <= 90 and float(i[1])<=180:
        print(True)
    else:
        print(False)


# for coords in open(0):
#     latitude, longitude = map(float, coords.strip('\n()').split(', '))
#     print(-90 <= latitude <= 90 and -180 <= longitude <= 180)