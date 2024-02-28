from datetime import datetime, timedelta
pattern = '%H:%M'
start, finish = [datetime.strptime(input(), pattern) for i in range(2)]

while (start + timedelta(minutes=45)) <= finish:

    print(start.strftime(pattern), '-', (start + timedelta(minutes=45)).strftime(pattern))
    start += timedelta(minutes=55)