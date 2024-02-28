def clock(number, count=1):
    if count < number:
        print(f'{str(count) * (number - count + 1) * 4:^16}')
        clock(number, count + 1)
        print(f'{str(count) * (number - count + 1) * 4:^16}')
    else:
        print(f'{str(count) * 4:^16}')


clock(4)

