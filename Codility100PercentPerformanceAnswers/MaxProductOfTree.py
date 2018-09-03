'''
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

Write a function:

def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].
'''


def solution(A):
    A.sort(reverse=True)
    positiveArray = [i for i in A if i > 0 ]
    negtiveArray = [i for i in A if i <=0 ]

    print(A)
    print(positiveArray)
    print(negtiveArray)

    if len(positiveArray) >= 3:
        result1 = positiveArray[0] * positiveArray[1] * positiveArray[2]
        if len(negtiveArray) >= 2:
            negtiveArray.sort()
            result2 = positiveArray[0] * negtiveArray[0] * negtiveArray[1]
            return max([result1, result2])
        else:
            return result1
    elif len(positiveArray) == 2:
        if len(negtiveArray) >= 2:
            negtiveArray.sort()
            return positiveArray[0] * negtiveArray[0] * negtiveArray[1]
        elif len(negtiveArray) == 1:
            return positiveArray[0] * positiveArray[1] * negtiveArray[0]
    elif len(positiveArray) == 1:
        negtiveArray.sort()
        return positiveArray[0] * negtiveArray[0] * negtiveArray[1]
    elif len(positiveArray) == 0:
        return negtiveArray[0] * negtiveArray[1] * negtiveArray[2]


if __name__ == '__main__':
    print(solution([5, -1, -2, -3, -3]))