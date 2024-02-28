from sys import exc_info
try:
    х = 1 / 0
except Exception as err:
    print(exc_info())