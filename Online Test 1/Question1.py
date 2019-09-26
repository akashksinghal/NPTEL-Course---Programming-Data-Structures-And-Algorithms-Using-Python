"""Here is a function isprimebad that takes a positive integer as input and returns True if the number is prime and False otherwise. 
There is an error in this function. 
Provide an input n, which is a positive integer, for which isprimebad produces an incorrect output.
"""
"""
import math

def isprimebad(n):
  if n < 2:
    return(False)
  else:
    for i in range(2, int(math.sqrt(n))):
      if n%i == 0:
         return(False)
    return(True)
"""
#INPUT
15