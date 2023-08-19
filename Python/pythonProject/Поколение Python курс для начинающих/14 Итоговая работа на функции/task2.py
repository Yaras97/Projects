# объявление функции
def get_shipping_cost(quantity):
    st = 0
    if n > 1:
        for i in range(n - 1):
            st += 120
        st = st + 1000
        return st
    else:
        return 1000

# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))