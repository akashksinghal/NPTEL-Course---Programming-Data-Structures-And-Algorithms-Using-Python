"""
Write a Python program that reads input from the keyboard (standard input). The input will consist of 
some number of lines of text. The input will be terminated by a blank line. The first line will consist 
of a single word to be interpreted as a pattern, after discarding the new line character. Your program 
should print the last line from the second line onward that contains an occurrence of the pattern. If no 
lines match the pattern, the program should print an empty line. You can assume that the input will have 
a non-empty pattern line. Recall that for a string s and a pattern p, s.find(p) returns the first 
position in s where p occurs, and returns -1 if p does not occur in s.
"""
K=input()
A=[]
while 1:
  s=input()
  if s=='':
    print(A[-1])
    break
  else:
    if s.find(K) !=-1:
      A.append(s)