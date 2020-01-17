''''
Write a function that takes a 'big' string and a 'small' string. The function
should return an array of of boolean, representing whether or not the small
string is present in the big string.

Input -
'this is a big string', ["this","yo","is","a","bigger","string","kappa"]

Solution 1 -
[True,False,True,True,False,True,False]
''''
def multiStringSearch(bigString, smallStrings):
    return [is_string_in(small_string,bigString) for small_string in smallStrings]

def is_string_in(small_string,bigString):
	for i in range(len(bigString)):
		if i+len(small_string) > len(bigString):
			break
		if is_string_in_helper(small_string,bigString,i):
			return True
	return False

def is_string_in_helper(small_string,bigString,index):
	left_big_index = index
	right_big_index = index+len(small_string)-1
	left_small_index = 0
	right_small_index = len(small_string)-1
	while left_big_index <= right_big_index:
		if bigString[left_big_index] != small_string[left_small_index] or bigString[right_big_index]!=small_string[right_small_index]:
			return False
		left_small_index += 1
		right_small_index -= 1
		left_big_index += 1
		right_big_index -= 1
	return True

''''
Solution 2 -
Create a Siffix Trie of the Big String
''''
def multiStringSearch(bigString, smallStrings):
	suffix_trie = ModifiedSuffixTrie(bigString)
	return [suffix_trie.contains(small_string) for small_string in smallStrings]

class ModifiedSuffixTrie:
	def __init__(self,string):
		self.root = {}
		self.populateSuffixFromString(string)

	def populateSuffixFromString(self,string):
		for i in range(len(string)):
			sub_string = string[i:]
			self.insert(sub_string)

	def insert(self,sub_string):
		node = self.root
		for char in sub_string:
			if char not in node:
				node[char] = {}
			node = node[char]

	def contains(self,string):
		node = self.root
		for char in string:
			if char not in node:
				return False
			else:
				node = node[char]
		return True

''''
Solution 3 -
Create a Trie of the smaller strings and check if the smaller string is
contained in the bigger string
''''

def multiStringSearch(bigString, smallStrings):
    trie = Trie()
	contained_small_strings = {}
	for small_string in smallStrings:
		trie.insert(small_string)
	for i in range(len(bigString)):
		subString = bigString[i:]
		trie_strings_contained_in_bigstring(subString,contained_small_strings,trie)
	return [(small_string in contained_small_strings) for small_string in smallStrings]

def trie_strings_contained_in_bigstring(subString,contained_small_strings,trie):
	current_node = trie.root
	for char in subString:
		if char not in current_node:
			break
		current_node = current_node[char]
		if trie.end_indicator in current_node:
			contained_small_strings[current_node[trie.end_indicator]] = 'True'

class Trie:
	def __init__(self):
		self.root = {}
		self.end_indicator = '*'

	def insert(self,string):
		current_node = self.root
		for char in string:
			if char not in current_node:
				current_node[char] = {}
			current_node = current_node[char]
		current_node[self.end_indicator] = string
