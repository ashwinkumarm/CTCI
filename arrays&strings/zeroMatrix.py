'''
Created on 04-Jun-2018

@author: Ashwin
'''

def zeroMatrix(matrix):
    firstRowZero = False
    firstColZero = False
    
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            firstRowZero = True
            break
        
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            firstColZero = True
            break
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            nullifyRow(matrix, i)
            
    for j in range(1, len(matrix[0])):
        if matrix[0][j] == 0:
            nullifyCol(matrix, j)
    
    if firstRowZero:
        nullifyRow(matrix, 0)
    
    if firstColZero:
        nullifyCol(matrix, 0)
        
    return matrix

def nullifyRow(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0
        
def nullifyCol(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0
        
def main():        
    matrix = [[1,0,1,2],[2,1,0,1], [1,2,3,4]]
    m = zeroMatrix(matrix)
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j])

main()
    