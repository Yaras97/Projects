def beegeek():
    try:
        value = 100
        return value
    except:
        value = 200
    else:
        value = 300
    finally:
        return value
print(beegeek())