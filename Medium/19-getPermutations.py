''''
Write a function that takes in array of intergers and returns all permutations
Sample Input -[1,2,3]
Output - [[1,2,3],[1,3,2],[2,3,1],[2,1,3],[3,2,1],[3,1,2]]
Solution 1 -
Time - O(N^2 * N!) | Space - O(N*N!)
''''

def getPermutations(array):
	permutations = []
	getPermutations_helper(array,[],permutations)
	return permutations

def getPermutations_helper(array,current_perm,permutations):
	if not len(array) and len(current_perm):
		permutations.append(current_perm)
	else:
		for i in range(len(array)):
			new_array = array[:i]+array[i+1:]
			new_perm = current_perm + [array[i]]
			getPermutations_helper(new_array,new_perm,permutations)
''''
Solution 2 - (Most Optimal solution using Backtracking algorithm)
Time - O(N*N!) | Space - O(N*N!)
''''

def getPermutations(array):
    permutations = []
	getPermutations_helper(array,permutations,0,len(array)-1)
	return permutations

def getPermutations_helper(array,permutations,lp,rp):
	if lp == rp:
		permutations.append(array[:])
	else:
		for i in range(lp,rp+1):
			swap(array,lp,i)
			getPermutations_helper(array,permutations,lp+1,rp)
			swap(array,lp,i)

def swap(array,i,j):
	array[i],array[j] = array[j],array[i]
