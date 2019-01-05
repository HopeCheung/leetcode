def window_slip(array, k):
	length = len(array)
	if length < k:
		return -1
	max_sum = 0
	for i in range(k):
		max_sum = max_sum + array[i]

	window_sum = max_sum
	for j in range(k, length - k):
		window_sum = window_sum + array[j] - array[j-k]
		max_sum = max(window_sum, max_sum)
	return max_sum