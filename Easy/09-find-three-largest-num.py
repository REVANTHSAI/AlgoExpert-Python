# Write a function that takes in array of intergers and returns a sorted array of three largest integers
# Time - O(N) Space - O(1)
def findThreeLargestNumbers(array):
	result = [None,None,None]
	for num in array:
			insert_into_result(result,num)
	return result

def insert_into_result(result,num):
	if result[2] == None or num > result[2]:
		shift_and_update(result,num,2)
	elif result[1] == None or num > result[1]:
		shift_and_update(result,num,1)
	elif result[0] == None or num > result[0]:
		shift_and_update(result,num,0)

def shift_and_update(result,num,index):
	for i in range(index+1):
		if i == index:
			result[i] = num
		else:
			result[i]=result[i+1]
