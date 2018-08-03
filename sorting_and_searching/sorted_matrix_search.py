def sorted_matrix_search(matrix, x):
    r = 0
    c = len(matrix[0]) - 1

    while r < len(matrix) and c >= 0:
        if matrix[r][c] == x:
            return True
        elif matrix[r][c] > x:
            c -= 1
        else:
            r += 1

    return False

matrix = [[15, 20, 40, 85], [20, 35, 80, 95], [30, 55, 96, 105], [40, 80, 100, 120]]
print(sorted_matrix_search(matrix, 55))


