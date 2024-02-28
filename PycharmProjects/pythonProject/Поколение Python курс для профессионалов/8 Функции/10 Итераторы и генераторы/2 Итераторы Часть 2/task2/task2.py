# def transpose(matrix):
#     return [list(row) for row in zip(*matrix)]

def transpose(mat):
    result = []
    for r in zip(*mat):
        print(r)
        result.append(list(r))
    return result


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in transpose(matrix):
    print(row)
