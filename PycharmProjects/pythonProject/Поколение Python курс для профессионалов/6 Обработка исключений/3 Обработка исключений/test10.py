def beegeek():
    try:
        value = 100
    except:
        value = 200
    else:
        value = 300
    finally:
        return value
print(beegeek())