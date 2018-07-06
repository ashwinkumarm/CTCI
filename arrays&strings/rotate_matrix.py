'''
Created on 04-Jun-2018

@author: Ashwin
'''


def rotate_matrix(matrix):
    
    if len(matrix) != len(matrix[0]) or len(matrix) == 0:
        return False
    
    n = len(matrix)
    
    for layer in range(int(n/2)):
        first = layer
        last = n - first - 1
        for i in range(first, last, 1):
            top = matrix[first][i]
            matrix[first][i] = matrix[last-i][first]
            matrix[last-i][first] = matrix[last][last-i]
            matrix[last][last-i] = matrix[i][last]
            matrix[i][last] = top
    
    for i in range(len(matrix)):
        print(matrix[i])
            
    return True


def main():
    matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
    
    rotate_matrix(matrix)


main()
