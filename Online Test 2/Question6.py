"""
Write a Python function intersect(l1,l2) that takes two sorted lists as arguments and returns the 
list of all elements common to both l1 and l2 in the same order that they appear in the two lists. 
If the same element occurs more than once in both lists, it should appear in the output exactly once.
"""
def intersect(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        return list(a_set & b_set) 
    else: 
        return []