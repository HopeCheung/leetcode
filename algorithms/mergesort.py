import time


def mergesort(array):
    def merge(lst1, lst2):
        if len(lst1) == 0:
            return lst2
        elif len(lst2) == 0:
            return lst1
        elif lst1[0] > lst2[0]:
            return [lst2[0]] + merge(lst1, lst2[1:])
        else:
            return [lst1[0]] + merge(lst1[1:], lst2)
        
    def divide(lst):
        if len(lst) == 1:
            return lst
        mid = len(lst) // 2
        left = divide(lst[:mid])
        right = divide(lst[mid:])
        return merge(left, right)
    
    return divide(array)

            
