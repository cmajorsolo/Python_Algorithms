def solution(N, M):
    resultArr = [0]
    startWith = 0
    loopTime = N

    while loopTime > 0:
        startWith = (startWith + M) % N
        if startWith in resultArr:
            return resultArr

        resultArr.append(startWith)
        loopTime -= 1



if __name__ == '__main__':
    print(solution(10, 3))