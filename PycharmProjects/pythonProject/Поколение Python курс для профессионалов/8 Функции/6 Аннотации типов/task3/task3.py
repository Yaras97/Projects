def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    result = dict()
    for i in range(1, len(matrix) + 1):
        result[i] = matrix[i-1]
    return result


matrix = [[1, 2, 3, 4, 5, 6, 7, 8]]

print(matrix_to_dict(matrix))