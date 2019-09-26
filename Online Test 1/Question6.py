"""Write a Python function subsequence(l1,l2) that takes two sorted lists as arguments and returns True if 
the the first list is a subsequence of the second list, and returns False otherwise.

A subsequence of a list is obtained by dropping some values. Thus, [2,3,4] and [2,2,5] are 
subsequences of [2,2,3,4,5], but [2,4,4] and [2,4,3] are not.
"""

def subsequence(lst1, lst2):
    l1, l2 = len(lst1), len(lst2)
    if l1 > l2: 
        return False
    i = j = 0
    d1, d2 = l1, l2
    while i < l1 and j < l2:
        while lst1[i] != lst2[j]:
            j += 1
            d2 -= 1
            if d1 > d2: 
                return False
        i, j, d1, d2 = i+1, j+1, d1-1, d2-1
        if d1 > d2:
            return False
    return True
