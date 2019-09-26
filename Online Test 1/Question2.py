"""Here is a function lexsortbad that takes a list of pairs of integers as input and returns 
them in lexicographically sorted order (i.e., dictionary order). There is an error is this function. 
Provide an input for which lexsortbad produces an incorrect output. 
Your input should be a list of pairs of integers of the form [(i1,j1),(i2,j2),...,(in,jn)].
"""
"""
def lexsortbad(l):
  for k in range(2):
    for j in range(len(l)-1):
      for i in range(len(l)-1):
        if l[i][k] > l[i+1][k]:
          (l[i],l[i+1]) = (l[i+1],l[i])
  return(l)
"""
#INPUT
[(1,2),(2,1)]