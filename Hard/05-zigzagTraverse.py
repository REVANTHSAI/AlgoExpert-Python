def zigzagTraverse(array):
    height = len(array)
    width = len(array[0])
    row,column = 0,0
    isGoingDown = True
    result = []
    while isArrayInBound(row,column,width,height):
        result.append(array[row][column])
        if isGoingDown:
            if column == 0 or row == height-1:
                isGoingDown = False
# If we are in the final row regardless of if we are in the first column. We have to go right.
# This sequence of if-conditions is important for [1,2,3,4,5] to work.
                if row == height-1:
                    column += 1
				else:
                    row += 1
            else:
                row += 1
                column -= 1

        else:
            if row == 0 or column == width-1:
                isGoingDown = True

# If we are in the final column regardless of if we are in the first row. We have to go down.
# This sequence of if-conditions is important for [[1],[2],[3],[4],[5]] to work.

                if column == width-1:
                    row += 1
                else:
                    column += 1
            else:
                row -= 1
                column += 1
    return result

def isArrayInBound(row,column,width,height):
    return row >= 0 and row < height and column >=0 and column < width

if __name__ == '__main__':
    test = [[1,2,3,4,5]]
    result = zigzagTraverse(test)
    print(result)
