"""Write a Python function sublist(l1,l2) that takes two sorted lists as arguments and returns True 
if the the first list is a sublist of the second list, and returns False otherwise.

A sublist of a list is a segment consisting of contiguous values, without a gap. 
Thus, [2,3,4] is a sublist of [2,2,3,4,5], but [2,2,4] and [2,4,5] are not."""

def sublist(A,B):
  flag=False
  if len(A) > len(B):
    return False
  for i in range(0,len(B)-len(A)+1):
      l1 = B[i:i+len(A)]
      l2 = A[0:]
      if  l1== A:
      	return True
  return False
