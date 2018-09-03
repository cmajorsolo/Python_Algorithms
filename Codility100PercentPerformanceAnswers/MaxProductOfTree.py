
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