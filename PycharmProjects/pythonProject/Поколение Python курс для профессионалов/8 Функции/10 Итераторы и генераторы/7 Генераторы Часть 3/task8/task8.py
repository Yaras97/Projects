def stop_on(itrable, obj):
    for i in itrable:
        if i == obj:
            break
        yield i

data = []

print(list(stop_on(data, 'stepik')))