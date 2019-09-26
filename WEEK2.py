#Write a function intreverse(n) that takes as input a positive integer n and returns the integer obtained by reversing the digits in n.
def intreverse(var):
    reverse=0
    while(var>0):
        rem=var%10
        reverse=(reverse*10)+rem
        var=var//10
    return reverse
#Write a function sumprimes(l) that takes as input a list of integers l and retuns the sum of all the prime numbers in l.
def sumprimes(liss):
    ssum=0
    for i in liss:
        flag=True
        if i>0:
            for j in range(2,int((i**0.5)+1)):
                if (i%j)==0:
                    flag=False
            if flag !=False and i!=1:
                ssum=ssum+i
#Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other symbols that appear in s. Your function should return True if s has matched brackets and False if it does not.
def matched(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0
