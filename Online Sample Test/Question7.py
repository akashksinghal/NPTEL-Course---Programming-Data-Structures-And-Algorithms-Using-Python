"""Write a Python program that reads input from the keyboard (standard input). The input will consist 
of some number of lines of text. The input will be terminated by a blank line. 
Your program should print every third line.
For instance:
"Spot the mistake
in the following argument",
Jack challenged
1+(-1+1)+(-1+1)+... = (1+ -1)+(1+ -1)+...
so therefore,
1 = 0
??

then the output should be:

Jack challenged
1 = 0
"""

i = 1
while 1:
    line = input()
    if line=='':
        break
    if i%3 == 0:
        print(line)
    i = i+1