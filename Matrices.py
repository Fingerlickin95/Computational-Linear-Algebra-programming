import numpy as np

#define matrix, a list of lists, remember we want it to be mutable. 
A = [[0,1,2,3],
    [1,-2,-5,4]]

B = [[10,-4,-1,0],
     [2,-8,-1,7],
     [4,1,-4,14],
     [6,10,-9,-3]]

C = [[11,-2],
     [1,1],
     [-1,-9]]

D = [[-5,0,1],
     [-7,3,3],
     [6,6,9]]

E = [[1,0],
     [0,-1]]

F = [[2,5,-6],
     [-8,1,-1],
     [-4, 3,9]]

G = [[2,2],
     [4,-4]]

#dimension checking for matrices
def check_dimension(A):
    assert type(A) is list, "matrix must be a list"
    rows = len(A)
    columns = len(A[0])
    dimensions=[]
    dimensions.append(rows)
    dimensions.append(columns)
    return dimensions

#matrices = [A,B,C,D,E,F]
#for i in matrices:
    print(check_dimension(i))

def compare_dimensions(matrix1,matrix2):
    A_dim = check_dimension(matrix1)
    B_dim = check_dimension(matrix2)
    if A_dim == B_dim:
        return True
    else:
        return False

#write matrix operation for matrix addition.

def construct_empty_matrix(matrix1):
    rows, cols = check_dimension(matrix1)
    new_matrix = [[0 for j in range(cols)] for i in range(rows)]
    print(f"constructed new matrix of {rows} rows & {cols} columns")
    return new_matrix

def matrix_addition(matrix1,matrix2):
    assert compare_dimensions(matrix1,matrix2) == True, "dimensions match" #call dimension check, if true, proceed
    new_matrix = construct_empty_matrix(matrix1) #construct empty matrix, set dims to matrix1 or 2
    for i in range(len(matrix1)): #loop over rows
        for j in range(len(matrix2[0])): #loop over columns
            new_matrix[i][j] = matrix1[i][j] + matrix2[i][j] #populate new matrix ij
    print(f"A + B ={new_matrix}")
    return new_matrix        

matrix_addition(E,G)
