def diskStacking(disks):
    disks.sort(key = lambda disk:disk[2])
    heights = [disk[2] for disk in disks]
    sequence = [None for _ in range(len(disks))]
    for i in range(1,len(heights)):
        current_disk = disks[i]
        for j in range(i):
            prev_disk = disks[j]
            if isStackable(prev_disk,current_disk):
                if heights[i] <= heights[j]+current_disk[2]:
                    heights[i] = heights[j]+current_disk[2]
                    sequence[i] =  j
    max_index = heights.index(max(heights))
    disk_result = constructDiskList(sequence,max_index,disks)
    return disk_result


def isStackable(above,below):
    return below[0] > above[0] and below[1] > above[1] and below[2] > above[2]

def constructDiskList(sequence,max_index,disks):
    disk_list = []
    current_index = max_index
    while current_index != None:
        disk_list.append(disks[current_index])
        current_index = sequence[current_index]
    return list(reversed(disk_list))
