"""
Here is a function to compute the third smallest value in a list of distinct integers. All the 
integers are guaranteed to be below 1000000. You have to fill in the missing lines. You can assume 
that there are at least three numbers in the list.
"""
def thirdmin(l):
  (mymin,mysecondmin,mythirdmin) = (1000000,1000000,1000000)
  for i in range(len(l)):
    # MY code below this line
    for j in range(i+1,len(l)):
      if l[i]>l[j]:
        temp=l[i]
        l[i]=l[j]
        l[j]=temp
  mymin=l[0]
  mysecondmin=l[1]
  mythirdmin=l[2]
    # MY code above this line
  return(mythirdmin)