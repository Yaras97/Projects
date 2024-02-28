def hash_function(obj):
    obj_str = str(obj)

    # Шаг 1: Вычисление значения выражения
    step1_result = sum(ord(obj_str[i]) * ord(obj_str[-(i + 1)]) for i in range(len(obj_str) // 2))

    # Шаг 2: Вычисление значения выражения
    step2_result = sum((-1) ** i * ord(obj_str[i]) * (i + 1) for i in range(len(obj_str)))

    # Шаг 3: Вычисление значения выражения (temp1 * temp2) % 123456791
    step3_result = (step1_result * step2_result) % 123456791

    return step3_result


array = [8022, 530.602391530928, 'lycmfojREEBSKNcNoIjM', False, {'написать': False, 'собеседник': True},
         (1448, True, -3913.85417440914, True),
         [True, True, 554, 'FCLRrFheVhkrubirMUts', -33242154218.4859, 885507704053.121]]

for obj in array:
    print(hash_function(obj))