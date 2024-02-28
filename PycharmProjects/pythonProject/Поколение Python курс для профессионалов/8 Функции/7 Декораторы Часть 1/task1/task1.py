def sandwich(func):
    def wrapper(*args, **kwargs):
        print("---- Верхний ломтик хлеба ----")
        result = func(*args, **kwargs)
        print("---- Нижний ломтик хлеба ----")
        return result

    return wrapper


@sandwich
def counter():
    for i in range(17):
        print(i)

counter()