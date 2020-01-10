''''
Question: Write a function that takes in array of strings and returns a list of anagrams.
Anagrams are strings made of exactly same letters, where order doesn't matter.
Sample Input - ["yo","act","flop","tac","cat","oy","olfp"]
Sample Output - [["yo","oy"],["flop","olfp"],["act","tac","cat"]]

O(N*L*LogL) Space | O(N) Time
L - Length of the longest strings
N - Number of strings in the input array
''''
def groupAnagrams(words):
	anagram = {}
	for word in words:
		sorted_word = "".join(sorted(word))
		if sorted_word in anagram:
			anagram[sorted_word].append(word)
		else:
			anagram[sorted_word] = [word]
	return anagram.values()
