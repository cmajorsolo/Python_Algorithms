def solution(A, B, C, D, E, F):
    resultArr = [0] * 6
    numbers = [A, B, C, D, E, F]
    numbers.sort()

    smallerThan6 = [i for i in numbers if i < 6]
    biggerThan6 = [i for i in numbers if i >= 6]

    if len(smallerThan6) < 3:
        return 'NOT POSSIBLE'
    elif len(smallerThan6) >= 3:
        resultArr[0] = smallerThan6[0]
        resultArr[2] = smallerThan6[1]
        resultArr[4] = smallerThan6[2]

    if resultArr[0] >= 2:
        return 'NOT POSSIBLE'
    else:
        if len(smallerThan6) > 3:
            i = len(smallerThan6) - 3
            if i == 1:
                resultArr[1] = smallerThan6[3]
                resultArr[3] = biggerThan6[0]
                resultArr[5] = biggerThan6[1]
            elif i == 2:
                resultArr[1] = smallerThan6[3]
                resultArr[3] = smallerThan6[4]
                resultArr[5] = biggerThan6[0]
            elif i == 3:
                resultArr[1] = smallerThan6[3]
                resultArr[3] = smallerThan6[4]
                resultArr[5] = smallerThan6[5]

        elif len(smallerThan6) == 3:
            resultArr[1] = biggerThan6[0]
            resultArr[3] = biggerThan6[1]
            resultArr[5] = biggerThan6[2]



    return str(resultArr[0])+str(resultArr[1])+':'+str(resultArr[2])+str(resultArr[3])+':'+str(resultArr[4])+str(resultArr[5])

    # return resultArr, smallerThan6, biggerThan6, numbers

#
# print(solution(1, 2, 3, 4, 5, 6))
# print(solution(0, 0, 0, 7, 8, 9))
# print(solution(1, 2, 3, 4, 5, 5))
# print(solution(2,4,5,9,6,9))
# print(solution(1 ,8, 3, 2, 6, 4))
# print(solution(0, 0, 0, 0, 0, 0))
# print(solution(0, 0, 0, 7, 8, 9))
# print(solution(2, 4, 5, 9, 5, 9))

import math
def phoneBillSolution(S):
    phoneNumbersArr = []
    timeArr = []
    for line in S.split(chr(10)):
        time = line.split(',')[0]
        phoneNumber = line.split(',')[1]
        seconds = get_sec(time)
        if phoneNumber in phoneNumbersArr:
            index = phoneNumbersArr.index(phoneNumber)
            originaltime = timeArr[index]
            newTime = originaltime + seconds
            timeArr[index] = newTime
        else:
            phoneNumbersArr.append(phoneNumber)
            timeArr.append(seconds)

    maxTime = max(timeArr)
    maxTimeIndex = timeArr.index(maxTime)
    del phoneNumbersArr[maxTimeIndex]
    del timeArr[maxTimeIndex]

    fee = 0
    for item in timeArr:
        if item < 300:
            fee += item * 3
        else:
            min = math.floor(item / 60)
            if item % 60 is not 0:
                min += 1
            fee += int(min) * 150
    return fee

def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


print(phoneBillSolution('00:01:07,400-234-090'+'\n'+'00:05:01,701-080-080'+'\n'+'00:05:00,400-234-090'))
