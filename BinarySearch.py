def binarySearch(element, S):
    S = sorted(S)
    middlePosition = len(S) // 2
    if len(S) == 1:
        if S[0] == element:
            return True
        else:
            return False

    if(element == S[middlePosition]):
        return True
    else:
        if element < S[middlePosition]:
            return binarySearch(element, S[:middlePosition])
        else:
            return binarySearch(element, S[middlePosition:])


if __name__ == '__main__':
    print(binarySearch(0, [8,7,6,5,4,3,2,1]))