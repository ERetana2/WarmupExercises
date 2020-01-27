# Python Warmup Exercises for Dr.Fuentes
"""
@author: Efrain Retana
"""
import numpy as np
# PROBLEM 1
def divisible(a,b):
    # if b can divide a and have no remainder, then it is divisible
    if a % b == 0:
        return True
    return False

# PROBLEM 2
def prime(n):
    # Check every number between 1-n to see if n is divisible by it and if it
    # is, then the number is prime
    for i in range(1,n):
        if n % i == 0:
            return False
    return True

# PROBLEM 3
def sum_digits(n):
    # reset remainder and sum to 0
    result = remainder = 0
    #while n > 0, take number's remainder and add to result
    while n > 0:
        remainder = n % 10
        n = int(n / 10)
        result = result + remainder
        
    return result

# PROBLEM 4
def reverse(s):
    return s[::-1] # reverse sequence
    
# PROBLEM 5
def remove_vowels(s):
    vowels = ('a','e','i','o','u')
    
    # for each letter that is a vowel inside of String s, then replace with ""
    for i in s.lower(): 
        if i in vowels:
            s = s.replace(i,"")
    return s

# PROBLEM 6
def pal(s):
    #reverse String then check if it is equivalent to original given String
    reverse = s[::-1]
    
    if s == reverse:
        return True
    return False

# PROBLEM 7
def max_array(A):
    maximum = 0
    # look through all the elements and update the max until there is no # higher
    for i in A:
        if i > maximum:
            maximum = i
    return maximum

# PROBLEM 8
def find(A,x):
    # iterate through all the set of numbers in the array until it finds x
    #  -if it does, then return i, else return -1
    for i in range(len(A)):
        if A[i] == x:
            return i
    return -1

# PROBLEM 9
def sum_array(A):
    sum = 0
    # iterate through each element and add it to sum, resulting in the total sum
    for i in A:
        sum = sum + i
    return sum

# PROBLEM 10
def replace_array(A,x,y):
    # create a temporary array 
#    newArr = A.copy()
#    # iterate through array until it finds x in newArr, then replace this x with y
#    for i in range(len(newArr)):
#        if newArr[i] == x:
#            newArr[i] = y
#    return newArr
    # create a numpy array  the assign all of its values to 0 ,
    # then check the values of A and replace them in B
    B = np.zeroes(len(A))
    for i in range(len(A)):
        if A[i] == x:
            B[i] == y
        else:
            B[i] = A[i]
    return B

# PROBLEM 11
def is_square(A):
    # compare size of rows vs size of columns while it is a square
    numRows = len(A)
    for i in range(len(A)):
        if numRows != len(A[i]):
            return False
        
    return True

# PROBLEM 12
def diagonal_sum(A):
    #sum the the main diagonal by adding all the elements from 0 - len(A) from
    # A[i][i]
    sum = 0
    for i in range(len(A)):
        sum = sum + A[i][i]
    return sum
    
# PROBLEM 13
def sec_diagonal_sum(A):
    # sum the second diagonal by adding all rows at [i] and column at len(A) - 1 - i
    sum = 0
    for i in range(len(A)):
        sum = sum + A[i][len(A) - i - 1]
    return sum
    
# PROBLEM 14
def diagonal(A):
    # create a new temporary 1D array, then iterate through the 2D array's
    # main diagonal, then append those elements to the 1D array
    newArray = []
    for i in range(len(A)):
        newArray.append(A[i][i]);
        
    return newArray

# PROBLEM 15
def sec_diagonal(A):
    # create a new temporary  1D array, then iterate through the 2D array's sec
    # diagonal, then append those elements to the 1D array
    newArray = []
    
    for i in range(len(A)):
        newArray.append(A[i][len(A) - i - 1])
        
    return newArray

# PROBLEM 16
def swap_rows(A,i,j):
    # create temp array, then a temporary swap variable to save the the row[i]
    # the swap row[i] with row[j] then set row[j] = the saved row[i]
    tempArr = A.copy()
    tempArr[[i,j]] = tempArr[[j,i]]
    return tempArr

# PROBLEM 17 ----------------------------------------------------
def swap_columns(A,i,j):
    # create temporary array, then swap the columns 
    tempArr = A.copy()
    tempArr[:,[i,j]] = tempArr[:,[j,i]]
    return tempArr
    

# PROBLEM 18        
def replace_max_array(A,x):
    #create temporary array, and variables to hold the position of the index of
    # max at row and column
    tempArr = A
    saveRow = saveCol = 0
    max = 0
    # iterate to find the max of the 2D array, then replace the saved row and 
    # column to the given number ,x
    for i in range(len(tempArr)):
        for j in range(len(tempArr[i])):
            if tempArr[i][j] > max:
                max = tempArr[i][j]
                saveRow = i
                saveCol = j
    tempArr[saveRow][saveCol] = x
    return tempArr
            
# PROBLEM 19
def greater_than_list(L,x):
    tempList = []
    # iterate through the given list that satisfies L[i] > x then append to the
    # new temporary list
    for i in range(len(L)):
        if L[i] > x:
            tempList.append(L[i])
    return tempList
        
# PROBLEM 20
def split(L):
    # create 2 temporaries for odd indices and one for even indices
    # then append odd counts to oddList and even to evenList
    evenList = []
    oddList = []
    for i in range(0,len(L),2):
        evenList.append(L[i])
    for i in range(1,len(L),2):
        oddList.append(L[i])
        
# PROBLEM 21
def merge(L1,L2):
    L1Count = L2Count = 0
    tempList = []
    # Compares the greatest value or smallets value vs the other list, then 
    # places its value into the temporary list
    if L1[L1Count] > L2[L2Count]:
        tempList.append(L2[L2Count])
        L2Count += 1
    elif L1[L1Count] < L2[L2Count]:
        tempList.append(L1[L1Count])
        L1Count +=1
    else:
        tempList.append(L1[L1Count])
        tempList.append(L2[L2Count])
        
    # If not all the numbers are placed into the temporary list,
    # the remaining numbers will be appended into the list
    currNum = 0
    List = []
    
    if L1Count < len(L1):
        List = L1
    elif L2Count < len(L2):
        List = L2
    while currNum < len(List):
        tempList.append(List[currNum])
        currNum += 1
    # IN CLASS PROBLEM 22
def mergeClass(L1,L2):
    L = []
    i = j = 0
    for i in range(len(L1) + len(L2)):
        if i == len(L1):
            L = L + L2[j:]
            break
        elif j == len(L2):
            L = L + L1[i:]
            break
        elif L1[i] < L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1
    return L
    
    
# PROBLEM 22
def splitPivot(L):
    leftSide = rightSide = []
    # if num in list is less than , then append to left side, else append to right
    for i in L:
        if i < L[0]:
            leftSide.append(i)
        else:
            rightSide.append(i)
    return leftSide, rightSide




# Test Methods
arr = [1,2,7]
secArr = [5,6,9]
print(mergeClass(arr,secArr))




