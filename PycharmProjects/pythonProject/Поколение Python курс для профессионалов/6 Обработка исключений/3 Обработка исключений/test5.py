def beegeek():
    try:
        value = 100
        return value
    finally:
        value = 300
        return value
print(beegeek())