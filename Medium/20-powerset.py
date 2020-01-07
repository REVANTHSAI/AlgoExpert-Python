# Write a function to return a powerset
# Input [1,2,3]
# Output [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

# O(2^n*n) time | O(2^n*n) space
# Total number of powerset = 2^n
# Average Length of powerset = n/2
# Time comp - 2^n * n/2
def powerset(array):
	subset = [[]]
	for ele in array:
		for i in range(len(subset)):
			current_subset = subset[i]
			subset.append(current_subset+[ele])
	return subset


if __name__ == "__main__":
    result = powerset([1,2,3])
    print(result)
