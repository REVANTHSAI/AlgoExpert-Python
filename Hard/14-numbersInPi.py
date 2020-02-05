def numbersInPi(pi, numbers):
    pi_list = list(pi)
    number_dict = {num: True  for num in numbers}
    min_spaces =  getMinimumSpaces(pi_list,number_dict,0,{})
    return -1 if min_spaces == float("inf") else min_spaces

def getMinimumSpaces(pi_list,number_dict,index,mem_cache):
    if index == len(pi_list):
        return -1
    if index in mem_cache:
        return mem_cache[index]
    minSpaces = float('inf')
    for i in range(index,len(pi_list)):
        suffix = pi_list[index:i+1]
        if ''.join(suffix) in number_dict:
             minSpacesInSuffix = 1+getMinimumSpaces(pi_list,number_dict,i+1,mem_cache)
             minSpaces = min(minSpacesInSuffix,minSpaces)
    mem_cache[index] = minSpaces
    return mem_cache[index]
