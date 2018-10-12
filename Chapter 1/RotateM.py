''' Rotate a matrix by 90 degrees'''
def rotatem(m):
    j = 0
    l = len(m) - 1
    ''' Initialize empty 2d matrix with similar attributes of original NxN matrix'''
    new_matrix = [[None for _ in range(len(m))] for _ in range(len(m))]
    ''' Fill each row element with rotated values'''
    for i in range(l + 1):
        for k in range (len(m[i])):
            new_matrix[i][k] = m[l][i]
            l -= 1
        k = 0
        l = len(m) - 1
    return new_matrix
''' Test cases - [[1, 2, 3], [4, 5, 6], [7, 8, 9]]'''
matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21,  22, 23, 24, 25]]
result = rotatem(matrix)
print (result)
