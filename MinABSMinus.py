# 100 % pass
def minAbsMinus(A):
    minResult = -1
    for p in range(0, len(A)-1):
        firstPart  = sum([A[i] for i in range(0, p+1)])
        secondPart = sum([A[i] for i in range(p+1, len(A))])
        result = abs(firstPart - secondPart)
        if minResult is -1:
            minResult = result
        elif minResult > result:
            minResult = result
    return minResult