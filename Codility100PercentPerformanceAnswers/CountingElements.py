def solution(N, A):
    result = [0] * N
    for item in A:
        if 1 <= item <= N:
            # increase X
            result[item-1] += 1
            # print(result, max)
        if item == N + 1:
            result = [max(result)] * N
    return result
'''
100% performance
'''
def solutionOnLine(N, A):
    result = [0] * N
    max_counter = 0
    current_max = 0
    for command in A:
        if 1<= command <= N:
            if max_counter > result[command - 1]:
                result[command -1] = max_counter
            result[command - 1] += 1
            if current_max < result[command - 1]:
                current_max = result[command -1]
        else:
            max_counter = current_max
    for index in range(0, N):
        if result[index] < max_counter:
            result[index] = max_counter
    return  result

if __name__ == '__main__':
    print(solutionOnLine(5, [3,4,4,6,1,4,4]))
    print(solution(6, [1,7,7,7,7,7]))