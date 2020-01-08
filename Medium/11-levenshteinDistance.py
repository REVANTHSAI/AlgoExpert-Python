# M - Len(Str1)
# N- Len(Str2)
# Time - O(MN) Space - O(MN)
def levenshteinDistance(str1, str2):
	mem = [[i for i in range(len(str2)+1)] for _ in range(len(str1)+1)]
	for i in range(1,len(str1)+1):
		mem[i][0] = mem[i-1][0]+1
	for i in range(1,len(mem)):
		for j in range(1,len(mem[0])):
			if str1[i-1] == str2[j-1]:
				mem[i][j] = mem[i-1][j-1]
			else:
				mem[i][j] = 1+min(mem[i-1][j],mem[i-1][j-1],mem[i][j-1])
	return mem[-1][-1]

# Time - O(MN) Space - O(min(M,N))
def levenshteinDistance(str1, str2):
	small = str1 if str2 > str1 else str2
	large = str1 if str1 >= str2 else str2
	even_mem = [i for i in range(len(small)+1)]
	odd_mem = [None for _ in range(len(small)+1)]
	for i in range(1,len(large)+1):
		if i % 2 == 0:
			current_mem = even_mem
			prev_mem = odd_mem
		else:
			current_mem = odd_mem
			prev_mem = even_mem
		current_mem[0] = i
		for j in range(1,len(small)+1):
			if large[i-1] == small[j-1]:
				current_mem[j] = prev_mem[j-1]
			else:
				current_mem[j] = 1 + min(current_mem[j-1],prev_mem[j],prev_mem[j-1])
	return even_mem[-1] if len(large)%2 == 0 else odd_mem[-1]
