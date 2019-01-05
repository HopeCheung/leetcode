def bucketSort(nums):
    bucket = [0] * (max(nums) + 1)
    for num in nums:
        bucket[num] = bucket[num] + 1
    result = []
    for i in range(len(bucket)):
        result.extend([i] * bucket[i])
    return result
###-----用于处理数据跨度不大的非负整数