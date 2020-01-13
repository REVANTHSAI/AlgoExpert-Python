''''
Question -
Sample Input - [8,4,2,1,3,6,7,9,5]
Sample Output - 25 Eg- ([])
Time - O(N^2) | Space - O(N)
Solution 1 -
1. Compare every element to the next element in the scores list.
2. If scores[i-1] < scores[i]. Then update the min rewards for i. result[i] = result[i-1]+1
3. If scores[i-1] > scores[i]. Then iterate back till the start of the list update minimum rewards for each member.
while j > 0 and scores[j-1] > scores[j]:
	result[j-1] = max(result[j-1],result[j]+1)
Here 'max' is important to handle edgecase inputs like - [8,4,2,1,3,6,7,9,5]
''''
def minRewards(scores):
	result = [1 for _ in scores]
	for i in range(1,len(scores)):
		if scores[i-1] < scores[i]:
			result[i] = result[i-1]+1
		elif scores[i-1] > scores[i]:
			j = i
			while j > 0 and scores[j-1] > scores[j]:
				result[j-1] = max(result[j-1],result[j]+1)
				j -= 1
	minNumberOfRewards = sum(result)
	return minNumberOfRewards
''''
Solution 2 -
Time - O(N) | Space - O(N)
''''
def minRewards(scores):
    result = [1 for _ in scores]
	for i in range(1,len(scores)):
		if scores[i-1] < scores[i]:
			result[i] = result[i-1]+1
	for i in reversed(range(len(scores)-1)):
		if scores[i] > scores[i+1]:
			result[i] = max(result[i],result[i+1]+1)
	return sum(result)
''''
Solution-3 (Most Optimal)
Time - O(N) | Space - O(N)
1. Calculate the different local mins in the scores list.
2. For each local min, iterate to the left and right of the scores list and update the min rewards list.
''''
def minRewards(scores):
	result =[1 for _ in scores]
    local_mins = getLocalMins(scores)
	for local_min_index in local_mins:
		expandFromLocalMins(scores,result,local_min_index)
	return sum(result)

def getLocalMins(scores):
	local_mins = []
	if len(scores) == 1:
		return[0]
	for i in range(len(scores)):
		if i == 0 and scores[i] < scores[i+1]:
			local_mins.append(i)
		if i == len(scores)-1 and scores[i-1] > scores[i]:
			local_mins.append(i)
		if i == 0 or i == len(scores)-1:
			continue
		if scores[i] < scores[i+1] and scores[i] < scores[i-1]:
			local_mins.append(i)
	return local_mins

def expandFromLocalMins(scores,result,local_min_index):
	# Expand to the left of Local Mins
	left_index =  local_min_index - 1
	while left_index >= 0 and scores[left_index] > scores[left_index+1]:
		result[left_index] = max(result[left_index],result[left_index+1]+1)
		left_index -= 1
	# Expand to the right of the local Min
	right_index = local_min_index + 1
	while right_index < len(scores) and scores[right_index] > scores[right_index-1]:
		result[right_index] = result[right_index-1]+1
		right_index += 1
