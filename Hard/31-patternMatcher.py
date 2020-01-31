''''
Time O(N^2+M)|Space O(N+M)
Sample Input ("xxyxxy", "gogopowerrangergogopowerranger")
Sample Output ["go", "powerranger"]
''''
def patternMatcher(pattern, string):
	if len(pattern) > len(string):
		return []

	# If patter doesnt start with X, update pattern to start with X
	new_pattern = updatePattern(pattern)
	is_pattern_updated = new_pattern[0] != pattern[0]

	# Get count of X,Y in patter and the first Y index
	pattern_count = {"x": 0, "y":0}
	first_y_index_in_pattern = getCountsAndFirstPos(new_pattern,pattern_count)
	if pattern_count['y'] != 0:
		for x_len in range(1,len(string)):
			y_len = (len(string) - (x_len * pattern_count['x'])) / pattern_count['y']
			if y_len <= 0 or y_len % 1 != 0:
				continue
			y_len = int(y_len)
			y_index_in_string = first_y_index_in_pattern * x_len
			x = string[:x_len]
			y = string[y_index_in_string:y_index_in_string+y_len]
			potentialMatch = map(lambda char: x if char == 'x' else y,new_pattern)
			if string == ''.join(potentialMatch):
				return [y,x] if is_pattern_updated else [x,y]
	else:
		x_len = len(string)/pattern_count['x']
		if x_len % 1 == 0:
			x_len = int(x_len)
			x= string[:x_len]
			potentialMatch = map(lambda char: x, new_pattern)
			if string == ''.join(potentialMatch):
				return [x,""] if not is_pattern_updated else ["",x]
	return []

# Returns the count of X and Y in the patter and start index of y
def getCountsAndFirstPos(pattern,pattern_count):
	first_y_index = None
	for i,char in enumerate(pattern):
		pattern_count[char] += 1
		if char == 'y' and first_y_index == None:
			first_y_index = i
	return first_y_index

def updatePattern(pattern):
	pattern_list = list(pattern)
	if pattern_list[0] == 'x':
		return pattern_list
	else:
		return list(map(lambda char: "x" if char == "y" else "y",pattern_list))
