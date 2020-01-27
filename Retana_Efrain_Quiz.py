"""
@title : Python Warmup Quiz
@author: Efrain Retana
@author : Jason Keith
"""
import numpy as np

def swap_first_and_last(L):
    # create a swap variable, then swap first and last elements
    swap = L[0]
    L[0] = L[-1]
    L[-1] = swap
    return L
def diagonal(A):
    # create a numpy array with zeroes then change the diagonal equal to
    # the given array
    tempArr = np.zeros((len(A),len(A)), dtype = int)
    for i in range(len(A)):
        tempArr[i][i] = A[i]
    return tempArr

def greater_than_list(L,x):
    # SOLUTION 1
    return [L[i] for i in range(len(L)) if L[i] > x]
    # SOLUTION 2
#    List = []
#    for i in range(len(L)):
#        if L[i] > x:
#            List.append(L[i])
#    return List
    
if __name__ == " __main__":
    
    arr = [1,2,3]
    print(swap_first_and_last(arr))
    
    diagonalTest = [1,2,3]
    print(diagonal(diagonalTest))

    List = [1,2,3,4,5,6,7]
    print(greater_than_list(List, 3))
    
    
    




    

