# Given an array of positive intergers representing coin denomination and a single
# non-negative interger representing a target amount of money, implement a fuction that
# returns the smallest number of coins needed to make change
# Input = 7, [1,5,10]
# Output = 3 (2*1+1*5)
# Time-O(N) Space-O(N)
def minNumberOfCoinsForChange(n, denoms):
	min_array = [float('inf') for _ in range(n+1)]
	min_array[0] = 0
	for coin_value in denoms:
		for amount in range(1,n+1):
			if amount >= coin_value:
				min_array[amount] = min(min_array[amount],1+min_array[amount-coin_value])
	return min_array[n] if min_array[n] != float('inf') else -1
