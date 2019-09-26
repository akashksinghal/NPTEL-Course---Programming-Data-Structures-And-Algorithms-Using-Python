"""Write a Python function maxaggregate(l) that takes a list of pairs of the form (name,score) as argument
, where name is a string and score is an integer. Each pair is to be interpreted as the score of the named
 player. For instance, an input of the form [('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),
 ('Ashwin',90)] represents two scores of 73 and 7 for Kohli, two scores of 33 and 90 for Ashwin and one 
 score of 122 for Pujara. Your function should compute the players who have the highest aggregate score 
 (aggegrate = total, so add up all scores for that name) and return the list of names of these players as 
 a list, sorted in alphabetical order. If there is a single player, the list will contain a single name.

For instance, maxaggregate([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Ashwin',90)]) 
should return ['Ashwin'] because the aggregate score of Kolhi is 80, of Ashwin is 123 and of Pujara 
is 122, of which 123 is the highest.
"""
def maxaggregate(tup):
  D={}
  for (a,b) in tup:
    if a in D:
      D[a]=D[a]+b
    else:
      D[a]=b
  maximum = max(D, key=D.get)
  A=[]
  for i in D:
    if D[i] == D[maximum]:
      A.append(i)
  A.sort()
  return A