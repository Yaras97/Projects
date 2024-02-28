def convert(string):
    lower_count = 0
    upper_count = 0
    for symbol in string:
        if symbol.islower():
            lower_count += 1
        if symbol.isupper():
            upper_count += 1
    return string.upper() if upper_count > lower_count else string.lower()


print(convert('BEEgeek'))