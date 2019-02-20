def GreatestCommonFactor(x, y):
	if y < x:
		x, y = y, x
	while x != 0:
		r = y % x
		x, y = r, x
	return y

