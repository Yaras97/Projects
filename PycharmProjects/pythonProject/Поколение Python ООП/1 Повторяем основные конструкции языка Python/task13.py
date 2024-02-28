def annual_return(start, percent, years):
    m = 1 + percent / 100
    for _ in range(years):
        start *= m
        yield start

for value in annual_return(70000, 8, 10):
    print(round(value))