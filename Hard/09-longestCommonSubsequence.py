
# Implement a function that returns the longestCommonSubsequence. A sub sequence is
# defined as a group of charecters that appear sequentially.
#
# Sample Input -
# ("ZXVVYZW", "XKYKZPW")
# Sample Output -
# ["X", "Y", "Z", "W"])
#
# Solution 1 -
# Time - O(NM * min(N,M)) | Space - O(NM * min(N,M))

def longestCommonSubsequence(str1, str2):
    seq_mat = [[[]for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
    for i in range(1,len(str2)+1):
        for j in range(1,len(str1)+1):
            if str2[i-1] == str1[j-1]:
                seq_mat[i][j] = seq_mat[i-1][j-1]+[str1[j-1]]
            else:
                seq_mat[i][j] = max(seq_mat[i][j-1],seq_mat[i-1][j],key=len)
    return seq_mat[-1][-1]




# Instead of saving the entire matrix just save the current and previous
# rows that are required
# Time - O(NM * min(N,M)) Space - O(Min(N,M)*Min(N,M))

def longestCommonSubsequence(str1, str2):
    smallString = str2 if str1 > str2 else str1
    bigString = str2 if str2 >= str1 else str1
    evenRow = [[] for _ in range(len(smallString)+1)]
    oddRow = [[] for _ in range(len(smallString)+1)]
    for i in range(1,len(bigString)+1):
        if i%2 == 0:
            prevRow = oddRow
            currentRow = evenRow
        else:
            prevRow = evenRow
            currentRow = oddRow
        for j in range(1,len(smallString)+1):
            if smallString[j-1] == bigString[i-1]:
                currentRow[j] = prevRow[j-1]+[smallString[j-1]]
            else:
                currentRow[j] = max(currentRow[j-1],prevRow[j],key=len)
    return evenRow[-1] if (len(bigString)%2 == 0) else oddRow[-1]

# Solution 3
# Most Optimal Solution -
# Time - O(MN) Space - O(MN)


def longestCommonSubsequence(str1, str2):
    subSequence = [[[None,0,None,None] for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
    for i in range(1,len(str2)+1):
        for j in range(1,len(str1)+1):
            if str2[i-1] == str1[j-1]:
                subSequence[i][j] = [str1[j-1],subSequence[i-1][j-1][1]+1,i-1,j-1]
            else:
                if subSequence[i-1][j][1] > subSequence[i][j-1][1]:
                    subSequence[i][j] = [None,subSequence[i-1][j][1],i-1,j]
                elif subSequence[i][j-1][1] >= subSequence[i-1][j][1]:
                    subSequence[i][j] = [None,subSequence[i][j-1][1],i,j-1]
    return constructSubSequence(subSequence)

def constructSubSequence(subSequence):
    i = len(subSequence)-1
    j = len(subSequence[0])-1
    result = []
    while i != 0 and j != 0:
        currentEntry = subSequence[i][j]
        if currentEntry[0] != None:
            result.append(currentEntry[0])
        i = currentEntry[2]
        j = currentEntry[3]
    return list(reversed(result))
