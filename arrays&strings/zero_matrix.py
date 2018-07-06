'''
Created on 04-Jun-2018

@author: Ashwin
'''


def zero_matrix(matrix):
    first_row_zero = False
    first_col_zero = False
    
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            first_row_zero = True
            break
        
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            first_col_zero = True
            break
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            nullify_row(matrix, i)
            
    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            nullify_col(matrix, j)
    
    if first_row_zero:
        nullify_row(matrix, 0)
    
    if first_col_zero:
        nullify_col(matrix, 0)
        
    return matrix


def nullify_row(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


def main():        
    matrix = [[1, 0, 1, 2], [2, 1, 0, 1], [1, 2, 3, 4]]
    m = zero_matrix(matrix)
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j])


main()
