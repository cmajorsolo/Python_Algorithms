
# 100% answer
def genomicRangeQuery(S, P, Q):
    result = []
    minValue = 100
    for i in range(0, len(P)):
        start = P[i]
        end = Q[i]
        temp = S[start:end+1]
        if 'A' in temp:
            minValue = 1
        elif 'C' in temp:
            minValue = 2
        elif 'G' in temp:
            minValue = 3
        elif 'T' in temp:
            minValue = 4
        result.append(minValue)

    return result




if __name__ == '__main__':
    print(genomicRangeQuery('CAGCCTA', [2, 5, 0], [4, 5, 6]))