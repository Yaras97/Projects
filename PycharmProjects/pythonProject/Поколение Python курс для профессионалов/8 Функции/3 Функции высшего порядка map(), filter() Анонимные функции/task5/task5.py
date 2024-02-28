def print_operation_table(operation, rows, cols):
    for i in range(1, rows + 1):
        row_values = [operation(i, j) for j in range(1, cols + 1)]
        print(*row_values)

        
print_operation_table(lambda a, b: a * b, 5, 5)