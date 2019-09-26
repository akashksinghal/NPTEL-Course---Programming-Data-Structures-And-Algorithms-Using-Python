"""A positive integer n is a sum of squares if n = i2 + j2 for integers i,j such that i ≥ 1 and j ≥ 1. 
For instance, 10 is a sum of squares because 10 = 12 + 32, and so is 25 (32 + 42). On the other hand, 
11 and 3 are not sums of squares.

Write a Python function sumofsquares(n) that takes a positive integer argument and returns True if the 
integer is a sum of squares, and False otherwise.
"""
def sumofsquares( n) : 
    i = 1 
    while i * i <= n : 
        j = 1
        while(j * j <= n) : 
            if (i * i + j * j == n) : 
                #print(i, "^2 + ", j , "^2" ) 
                return True
            j = j + 1
        i = i + 1
          
    return False