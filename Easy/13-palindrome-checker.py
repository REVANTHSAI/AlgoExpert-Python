# Note - String concatenation takes O(N^2) time. So try to avoid it
# Iterative
# Time Complexity - O(N)
# Space Complexity O(1)
def isPalindrome(string):
    first_ptr = 0
	last_ptr = len(string)-1
	while first_ptr != last_ptr and first_ptr < last_ptr:
		if string[first_ptr] == string[last_ptr]:
			first_ptr += 1
			last_ptr -= 1
		else:
			return False
	return True

# Reccursive
# Time Complexity - O(N)
# Space Complexity O(N)
def isPalindrome(string,i=0):
    j= len(string)-1-i
    return True if i >= j else string[i] == string[j] and isPalindrome(string,i+1)
