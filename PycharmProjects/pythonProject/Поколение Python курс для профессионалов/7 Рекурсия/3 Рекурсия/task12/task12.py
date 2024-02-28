def process_number(n):
    print(n)
    if n <= 0:
        return
    process_number(n - 5)
    if n >= 0:
        print(n)


process_number(int(input()))