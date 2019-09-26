"""Here is a function to compute the largest of four input integers. You have to fill in the missing 
lines.
"""
def max4(w,x,y,z):
  if w >= x and w >= y and w >= z:
    maximum = w
  # Your code below this line
  elif x>=w and x>=y and x>=z:
    maxmimum =x
  elif y>=w and y>=x and y>=z:
    maximum = y
  else:
    maximum = z
  # Your code above this line
  return(maximum)


