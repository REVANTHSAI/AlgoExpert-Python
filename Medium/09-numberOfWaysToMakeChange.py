# Given an array of positive intergers that represent coin denominations and a
# Single non-negative interger representing a target amount of money. Write an function
# that return number of ways to derive change for the target amount.
# Sample Input - 6, [1,5]
# Smaple Output - 2
# Space O(N) Time O(N)
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for _ in range(n+1)]
	ways[0] = 1
	for coin_value in denoms:
		index = 1
		for index in range(1,n+1):
			if index >= coin_value:
				ways[index] += ways[index-coin_value]
	return ways[n]

				
