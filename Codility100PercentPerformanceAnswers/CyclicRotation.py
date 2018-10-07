def solution(A, K):
    if K == len(A) or not A:
        return A
    else:
        if K > len(A):
            K = K % len(A)
        return A[-K:] + A[:-K]

if __name__ == '__main__':
    print(solution([5, -1000], 1))
    print(solution([2,3,4,5,6,7,1], 8))
    print(solution([], 5))