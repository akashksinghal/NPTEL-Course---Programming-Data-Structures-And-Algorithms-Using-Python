"""Write a Python function repeated(l) that takes a list of immutable values as argument. 
The function should return the number of values that are repeated in the input list.

For instance, repeated([1,17,22,17,23,17]) should return 1 because only 1 value, 17 is repeated. 
Likewise repeated(["the","higher","you","climb","the","further","you","fall"]) is 2 becaues 2 values,
 "the" and "you", are repeated."""

def repeated(lis):
    uni=[]
    for i in lis:
        if i not in uni:
            uni.append(i)
    A=0
    for i in uni:
        M=0
        for j in lis:
            if j==i:
                M=M+1
                if M>1:
                    A=A+1
                    break
    return A
    