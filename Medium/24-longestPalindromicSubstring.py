''''
Question -
Write a function that, given a string returns its longest palindromice sub_string.
Sample Input - "ababyzzyxf"
Sample Output - "xyzzyx"

Solution 1 - (Optimal)
O(N^2) Time | O(1) Space
Steps -
For each charecter in the string check if the charecter is the middle of a
an odd Palindrom or an even Palindrome.
''''

def longestPalindromicSubstring(string):
	max_palindrome = [0,0]
    # Caulate odd and even Palindrome at every charecter of the string
    # Then save the max length Palindrome index in max_palindrome
    for i in range(1,len(string)):
		odd_palindrome = getPalindromicSubSting(string,i-1,i+1)
		even_palindrome = getPalindromicSubSting(string,i-1,i)
		current_palindrome = max(odd_palindrome,even_palindrome,key = lambda x: x[1]-x[0])
		max_palindrome = max(max_palindrome,current_palindrome,key = lambda x: x[1]-x[0])
	return string[max_palindrome[0]:max_palindrome[1]+1]

def getPalindromicSubSting(string,p1,p2):
	while p1 >= 0 and p2 <= len(string)-1:
		if string[p1] != string[p2]:
			break
		p1 -= 1
		p2 += 1
	return [p1+1,p2-1]


''''
Solution - 2
Calculate all the possible sub_string and find the longest possible
Palindrome
O(N^3) Time | O(1) Space
''''
def longestPalindromicSubstring(string):
	if len(string) < 2:
		return string
    max_palindrome_p1 = None
	max_palindrome_p2 = None
	max_palindrome_len = 0
	p1 = 0
	while p1 < len(string):
		p2 = p1+1
		while p2 < len(string):
			if string[p1] == string[p2] and isPalindrom(string[p1:p2+1]):
					if (p2-p1) > max_palindrome_len:
						max_palindrome_len = p2-p1
						max_palindrome_p1 = p1
						max_palindrome_p2 = p2
			p2 += 1
		p1 += 1
	return string[max_palindrome_p1:max_palindrome_p2+1]


def isPalindrom(sub_string):
	start_index = 0
	end_index = len(sub_string)-1
	while start_index < end_index:
		if sub_string[start_index] != sub_string[end_index]:
			return False
		start_index += 1
		end_index -= 1
	return True
