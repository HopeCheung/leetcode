def require(A, n, max_num):
    num, total = 1, 0
    for i in range(n):
        total = total + A[i]
        if total > max_num:
            total = A[i]
            num = num + 1
    return num
            

def upper_band(A, n, k):
    low = max(A)
    high = sum(A)
    while low < high:
        mid = (low + high) // 2
        result = require(A, n, mid)
        if result > k:
            low = mid + 1
        else:
            high = mid
    return low

def imbalance(A, n, k):
    limit = upper_band(A, n, k+1)  #split into k+1 group
    average = sum(A) / (k+1)
    result = []
    index = 0
    for i in range(k+1):
        one_elem = 0
        while one_elem <= limit and index < n:
            one_elem = one_elem + A[index]
            index = index + 1
        if index == n and one_elem <= limit:
            result.append(one_elem)
        else:
            index = index - 1
            one_elem = one_elem - A[index]
            result.append(one_elem)
    return max([abs(elem - average) for elem in result])

imbalance([1,4,5,3,2,6,8,9,7], 9, 2)
#https://blog.csdn.net/u011947630/article/details/81606259
