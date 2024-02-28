def parse_ranges(ranges):
    for i in ranges.split(','):
        dig = i.split('-')
        yield from range(int(dig[0]), int(dig[-1]) + 1)


print(*parse_ranges('1-2,4-4,8-10'))

