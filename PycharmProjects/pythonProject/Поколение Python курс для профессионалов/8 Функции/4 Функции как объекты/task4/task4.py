def polynom(x, values=set()):
    result = x**2 + 1
    values.add(result)
    polynom.values = values
    return result


for i in range(-100, 100):
    polynom(i)

print(*sorted(polynom.values))