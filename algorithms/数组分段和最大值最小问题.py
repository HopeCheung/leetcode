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

