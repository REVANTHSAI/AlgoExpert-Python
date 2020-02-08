# Time - O(N)Space - O(A)
A - Number of unique charecters in string
def longestSubstringWithoutDuplication(string):
	string_last_seen = {}
	substring_range = [0,1]
	start_index = 0
	for i, char in enumerate(string):
		if char in string_last_seen:
			start_index = max(start_index,string_last_seen[char]+1)
		if substring_range[1] - substring_range[0] < i+1 - start_index:
			substring_range = [start_index,i+1]
		string_last_seen[char] = i
	return string[substring_range[0] : substring_range[1]]
