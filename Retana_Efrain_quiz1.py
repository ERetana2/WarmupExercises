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
    
if __name__ == "__main__":  
    L = [1, 5, 8, 7, 9, 3, 0, 4, 2, 6]  
    swap_first_and_last(L)
    print(L)   # [6, 5, 8, 7, 9, 3, 0, 4, 2, 1]
    
    
    A = np.array([2,4,6,8])
    D = diagonal(A)
    print(D)
    
    ''' 
    Output: 
    [[2. 0. 0. 0.]
     [0. 4. 0. 0.]
     [0. 0. 6. 0.]
     [0. 0. 0. 8.]]
    '''
    
    L = [1, 9, 3, 0, 4, 2, 5, 8, 7, 6]
    L3 = greater_than_list(L,3)
    print(L3) # [9, 4, 5, 8, 7, 6]
    
    L7 = greater_than_list(L,7)
    print(L7) # [9, 8]
          
    L13 = greater_than_list(L,13)
    print(L13) # [] 
    
    




    

