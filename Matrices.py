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

H = [[10,-4,-1,0],
     [2,-8,-1,7],
     [4,1,-4,14],
     [6,10,-9,-3]]

#dimension checking for matrices
def check_dimension(matrix1:list)->list : 
    """
    returns dimensions of the argument matrix in list format    
    :param matrix1: 
    :return: eg. [2,4]
    :rtype: List
    """
    assert type(matrix1) is list, "matrix must be a list"
    rows = len(matrix1)
    columns = len(matrix1[0])
    dimensions=[]
    dimensions.append(rows)
    dimensions.append(columns)
    return dimensions

#matrices = [A,B,C,D,E,F]
#for i in matrices:
    #print(check_dimension(i))

def compare_dimensions(matrix1,matrix2):
    """
    calls check_dimension function to return True if dimensions(list) match
    
    :param matrix1
    :param matrix2    """
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
    assert compare_dimensions(matrix1,matrix2) == True, f"dimensions don't match, {check_dimension(A)} versus {check_dimension(B)}" #call dimension check, if true, proceed
    new_matrix = construct_empty_matrix(matrix1) #construct empty matrix, set dims to matrix1 or 2
    for i in range(len(matrix1)): #loop over rows
        for j in range(len(matrix2[0])): #loop over columns
            new_matrix[i][j] = matrix1[i][j] + matrix2[i][j] #populate new matrix ij
    print(f"A + B ={new_matrix}")
    return new_matrix        

def scalar_multiplication(matrix1,scalar: int):
    """
    Performs scalar matrix multiplication k*[A]    
    :param matrix1: Enter matrix
    :param scalar: Enter a scalar
    """
    new_matrix = construct_empty_matrix(matrix1) #container to populate with values
    for i in range(len(matrix1)): #iterate rows
        for j in range(len(matrix1[0])): #iterate cols
            new_matrix[i][j] = scalar*matrix1[i][j] 
    return new_matrix


def conformability_condition(matrix1,matrix2): #Checks inner dimensions for conformity
    dimensions_A = check_dimension(matrix1)
    dimensions_B = check_dimension(matrix2)
    
    rows_A = dimensions_A[0] #outputs rows
    cols_A = dimensions_A[1]
    rows_B = dimensions_B[0] 
    cols_B = dimensions_B[1]

    assert cols_A == rows_B, print(f"inner dimensions mismatch, A dimensions {dimensions_A} versus B dimensions{dimensions_B}")
    new_matrix = [[0 for j in range(cols_B)] for i in range(rows_A)] #list comp for generating empty matrices
    print(f"constructed new matrix of {rows_A} rows & {cols_B} columns")
    return new_matrix

def dot_product(matrix1,matrix2):
    shell = conformability_condition(matrix1,matrix2)
    for i in range(len(shell)):
        print(f"looping through row {i+1}")
        for j in range(len(shell[0])):
            print(f"accessing column {j}")
            shell[i][j] = 0 #init empty shell vector
            print(f"accessing empty vector {i},{j}")
            for k in range(len(matrix1[0])): #loop to populate shell vectors 
                shell[i][j] += matrix1[i][k] * matrix2[k][j]
    print(shell)
    return shell

dot_product(A,B)
