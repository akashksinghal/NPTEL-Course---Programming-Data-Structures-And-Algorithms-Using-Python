"""
Write a Python function sumof3squares(n) that takes a positive integer argument and returns True if 
the integer is a sum of three squares, and False otherwise.
"""
def sumof3squares(n):
  i=1
  while i*i<=n:
    j=1
    while j*j<=n:
      k=1
      while k*k<=n:
        if (i*i + j*j + k*k ==n):
          return True
        k=k+1
      j=j+1
    i=i+1
  return False