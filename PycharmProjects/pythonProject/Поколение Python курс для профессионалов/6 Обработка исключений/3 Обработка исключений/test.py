def num_return():
    try:
        x = [100]
        return x
    finally:
        x[0] = 90


print(num_return())
