"""
A list is a non-decreasing if each element is at least as big as the preceding one. 
For instance [], [7], [8,8,11] and [3,19,44,44,63,89] are non-decreasing, while [3,18,4] and 
[23,14,3,14,3,23] are not. Here is a recursive function to check if a list is non-decreasing. 
You have to fill in the missing argument for the recursive call.
"""

def nondecreasing(l):
  if l==[] or len(l) == 1:
    return(True)
  else:
    return(nondecreasing(l[1:]) if l[0] <= l[1] else False)