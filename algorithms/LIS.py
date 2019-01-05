def LIS(nums):
	def binary_search(target, nums):
		l, r = 0, len(nums) - 1
		while l <= r:
			mid = (l + r) // 2
			if nums[mid] == target:
				return mid
			elif nums[mid] < target:
				l = mid + 1
			else:
				r = r - 1
		return l

	res = []
	for num in nums:
		pos = binary_search(num, res)
		if pos >= len(res):
			res.append(num)
		else:
			res[pos] = num
	return len(res)

def DP_LIS(nums):
	dp = [0] * len(nums)
	dp[0] = 1
	for i in range(1, len(nums)):
		check = [dp[j]+1 for j in range(i) if nums[i] > nums[j]]
		dp[i] = 1 if check == [] else max(check)
	return max(dp)

#https://blog.csdn.net/George__Yu/article/details/75896330
