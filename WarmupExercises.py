# Python Warmup Exercises for Dr.Fuentes
"""
Created on Sat Jan 25 00:31:18 2020

@author: Efrain Retana
"""
def sumOfDigits (n):
    remainder =  n % 10
    return remainder + sumOfDigits(n/10)

print(sumOfDigits(12))