def get_min_max(data):
    if data == []:
        return None
    else:
        return min(enumerate(data), key=lambda x: x[1])[0], max(enumerate(data), key=lambda x: x[1])[0]


data = [-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58, -37, -100, 5, 75, 54, -79, -72, -2, 61, -16, -9, 89, -44, -30, -100, 96, -100, 1, 2, -99, 96]

print(get_min_max(data))

