def imbalance(A, n, k):
	a = sum(A) / (k+1)
	w = [[] for i in range(k+1)]
	dp =[[0 for j in range(n)] for i in range(k+1)]

	for i in range(n):
		dp[i][0] = abs(sum(A[:i+1]) - a)
	for j in range(k+1):
		dp[0][j] = max(abs(A[0] - a), a)
	dp[0][0] = abs(A[0] - a)

	for i in range(1, n):
		for j in range(1, k+1):
			max1 = max(dp[i-1][j-1], abs(A[j] - a))
			max2 = max(dp[i-1][j], a)
			max3 = max(dp[i][j-1], abs(sum(w[i]) + A[j] - a))
			dp[i][j] = max(max1, max2, max3)
			if dp[i][j] == max1:
				w[i] = [A[j]]
			elif dp[i][j] == max3:
				w[i].append(A[j])
	return dp[k][n-1]
