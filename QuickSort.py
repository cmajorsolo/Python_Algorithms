def quickSort(S):
    if len(S) < 1:
        return S
    else:
        return quickSort([x for x in S[1:] if x < S[0]]) + [S[0]] + quickSort([x for x in S[1:] if x > S[0]])


if __name__ == '__main__':
    print(quickSort([6,5,4,3,2,1]))