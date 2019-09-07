flattened = [item for sublist in l for item in sublist]

def diagonalDifference(arr):
    '''Two rolling windows one starts from 0 the other from -1
    0 1 2 ...
    -1 -2 -3 ...'''
    rightSum = 0
    leftSum = 0
    forwardWindow = 0
    reverseWindow = -1
    for row in arr:
        rightSum += row[forwardWindow]
        leftSum += row[reverseWindow]
        forwardWindow += 1
        reverseWindow -= 1
    return abs(rightSum - leftSum)
