def fourNumberSum(array, targetSum):
    result = []
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            temp_map = {}
            two_num_sum = array[i]+array[j]
            remaining_two_num_sum = targetSum-two_num_sum
            for index in range(len(array)):
                if index == i or index == j:
                    continue
                remaining_sum = remaining_two_num_sum - array[index]
                if (remaining_sum) in temp_map:
                    result.append([array[i],array[j],array[index],remaining_sum])
                    break
                else:
                    temp_map[array[index]] = True
    return result

if __name__ == '__main__':
    result = fourNumberSum([7,6,4,-1,1,2],16)
    print(result)
