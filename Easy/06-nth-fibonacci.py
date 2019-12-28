# Write a function that takes in an integer and return Nth Fibonacci Number
# Reccursive Solution -
#Time Complexity - O(2^N)
#Space Complexity - O(N)
def getNthFib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return getNthFib(n-2) + getNthFib(n-1)
    pass


# Above reccursice solution is very naive and has lots of repeated calculations.
# To remoive this ambiguity we save results to a hashmap and use them for later calculations
# Time Complexity - O(N)
# Space Complexity - O(N)
def getNthFib(n,memorize={1:0, 2:1}):
    if n in memorize:
        return memorize[n]
    else:
        memorize[n] = getNthFib(n-1,memorize) + getNthFib(n-2,memorize)
        return memorize[n]

#### Most Optimal #####
# Iterative Solution
# Time Complexity - O(N)
# Space Complexity - O(1)
def getNthFib(n):
    arr = [0,1]
    i = 2
    while i < n:
        sum = arr[0]+arr[1]
        arr[0]=arr[1]
        arr[1]=sum
        i += 1
    return arr[1] if n>1 else arr[0]
