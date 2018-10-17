''' Convert entire row and column to zeros, if a zero is encountered in the matrix'''
from collections import defaultdict

def change2zero(m):
    save_index = []
    new_matrix = m[:]
    ''' Save all the indexes of elements containing zeroes in the format (a,b), where a is the index of matrix, and
     b is he index of zero within that matrix'''
    for i in range(len(m)):
        for k in range(len(m[i])):
            if m[i][k] == 0:
                save_index.append(tuple([i,k]))
    ''' Change all the values for the required rows and columns to zeros, by using the output obtained above'''
    for p, q in save_index:
        for each in m:
            if all([v == 0 for v in each]):
                continue
            if m.index(each) == p:
                new_matrix[p] = [0 for _ in range(len(each))]
            else:
                new_matrix[m.index(each)][q] = 0

    return (new_matrix)

''' Test Cases:
[[1, 2, 0, 4], [6, 7, 8, 9], [11, 12, 13, 0], [16, 17, 18, 19], [21,  22, 23, 24]]
[[1, 2, 3], [6, 7, 8], [11, 12, 13], [0, 17, 18]]
[[1, 2], [0, 0], [11, 12]]'''
matrix = [[1, 2, 0, 4], [6, 7, 8, 9], [11, 12, 13, 0], [16, 17, 18, 19], [21,  22, 23, 24]]
result = change2zero(matrix)
print (result)
