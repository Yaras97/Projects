def get_digits(number: int | float) -> list[int]:
    return list(map(int, filter(lambda x: x.isdigit(), str(number))))


print(*get_digits.__annotations__.keys())
print(*get_digits.__annotations__.values())