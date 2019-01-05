def quick_sort(nums, left, right):
    if len(nums) == 0 or left >= right:
        return
    split = random_partition(nums, left, right)
    quick_sort(nums, left, split - 1)
    quick_sort(nums, split + 1, right)

def random_partition(nums, left, right):
    b = random.randint(left, right)
    nums[b], nums[right] = nums[right], nums[b]
    return partition(nums, left, right)
    
def partition(nums, left, right):
    pivot = nums[right]
    split = left - 1
    for j in range(left, right):
        if nums[j] <= pivot:
            nums[j], nums[split + 1] = nums[split+1], nums[j]
            split = split + 1
    nums[right], nums[split+1] = nums[split+1], nums[right]
    return split + 1

quick_sort([2,1,3,5,4], 0, 4)