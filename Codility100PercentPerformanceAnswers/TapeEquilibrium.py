'''
My solution. Correctness 100%. Performance is O(n * n)
'''
def solution(A):
    minimalDifference = -1

    if len(A) == 1:
        return 0
    for P in range(1, len(A)):
        firstPart = A[:P]
        secondPart = A[P:]
        if minimalDifference < 0:
            minimalDifference = abs(sum(firstPart) - sum(secondPart))
        elif minimalDifference > abs(sum(firstPart) - sum(secondPart)):
            minimalDifference = abs(sum(firstPart) - sum(secondPart))
    return minimalDifference

'''
Solution from https://codesays.com/2014/solution-to-tape-equilibrium-by-codility/
Performance 100%
'''
def solutionB(A):
    head = A[0]
    tail = sum(A[1:])
    min_dif = abs(head - tail)
    for index in range(1, len(A)-1):
        head += A[index]
        tail -= A[index]
        if abs(head-tail) < min_dif:
            min_dif = abs(head-tail)
    return min_dif

if __name__ == '__main__':
    # print(solution([3,1,2,4,3]))
    # print(solution([1]))
    print(solution([3,2]))