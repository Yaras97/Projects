def cubes_of_odds(num):
    return (i**3 for i in num if i % 2 == 1)


data = filter(lambda x: x % 13, range(101, 982))

print(*cubes_of_odds(data))