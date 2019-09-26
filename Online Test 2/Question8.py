"""Write a Python function maxaverage(l) that takes a list of pairs of the form (name,score) as argument, 
where name is a string and score is an integer. Each pair is to be interpreted as the score of the named 
player. For instance, an input of the form [('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),
('Ashwin',90)] represents two scores of 73 and 7 for Kohli, two scores of 33 and 90 for Ashwin and one 
score of 122 for Pujara. Your function should compute the players who have the highest average score 
(average = total across all scores for that player divided by number of entries) and return the list of 
names of these players as a list, sorted in alphabetical order. If there is a single player, the list will
 contain a single name.

For instance, maxaverage([('Kohli',73),('Ashwin',33),('Kohli',7),('Pujara',122),('Ashwin',90)]) should 
return ['Pujara'] because the average score of Kolhi is 40 (80 divided by 2), of Ashwin is 61.5 
(123 divided by 2) and of Pujara is 122 (122 divided by 1), of which 122 is the highest.
"""
def maxaverage(tup):
  D={}
  R={}
  for (a,b) in tup:
    if a in D:
      D[a]=D[a]+b
      R[a]=R[a]+1
    else:
      D[a]=b
      R[a]=1
  for i in R:
    D[i]=D[i]/R[i]
  maximum = max(D, key=D.get)
  A=[]
  for i in D:
    if D[i] == D[maximum]:
      A.append(i)
  A.sort()
  return A