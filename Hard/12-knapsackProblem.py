''''
Sample Input -
[[1,2],[4,3],[5,6],[6,7]],10
Sample Output -
[10,[1,3]]
''''
# O(nc) Time | O(nc) Space
def knapsackProblem(items, capacity):
    values = [[0 for _ in range(capacity+1)] for _ in range(len(items)+1)]
    for i in range(1,len(items)+1):
        for j in range(1,capacity+1):
            current_capacity = j
            current_weight = items[i-1][1]
            current_value = items[i-1][0]
            if current_capacity < current_weight:
                values[i][j] = values[i-1][j]
            else:
                value_without_current_item = values[i-1][j]
                value_before_inserting_current_item = values[i-1][j-current_weight]
                value_after_inserting_current_item = value_before_inserting_current_item + current_value
                values[i][j] = max(value_without_current_item,value_after_inserting_current_item)
    max_total_value = values[-1][-1]
    index_list = constructIndex(values,items)
    return [max_total_value,index_list]

def constructIndex(values,items):
    index_list = []
    i = len(values)-1
    j = len(values[0])-1
    while j != 0 and i != 0:
        if values[i][j] != values[i-1][j]:
            index_list.append(i-1)
            j = j-(items[i-1][1])
        i = i-1
    return list(reversed(index_list))
