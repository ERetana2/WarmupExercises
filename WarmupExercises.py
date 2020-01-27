# Python Warmup Exercises for Dr.Fuentes
"""
Created on Sat Jan 25 00:31:18 2020

@author: Efrain Retana
"""
# PROBLEM 2
def isPrimeNumber(n):
    for i in range(n):
        if n % i == 0:
            return False
    return True

# PROBLEM 3
    
# Test Methods
    isPrimeNumber(5)