''''
Give a string write a function to create a trie that contains all possible suffx of the string.
Also, write a function to check if a string is a suffix of the input string.
Trie Construction -
Time - O(N^2) Space - O(N)
Contains Func -
Time - O(N) Space - O(N)
''''
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
		for i in range(len(string)):
			self.insertSubString(i,string)

	def insertSubString(self,index,string):
		current_node = self.root
		for i in range(index,len(string)):
			if string[i] not in current_node:
				current_node[string[i]] = {}
			current_node = current_node[string[i]]
		current_node[self.endSymbol] = True

    def contains(self, string):
		current_node = self.root
		for char in string:
			if char not in current_node:
				return False
			current_node = current_node[char]
		return self.endSymbol in current_node
