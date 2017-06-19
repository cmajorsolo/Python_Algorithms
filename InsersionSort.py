def insertionSort(alist):
    for i in range(0,len(alist)-1):
        j = i
        while j >= 0:
            if alist[j] > alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
            j -= 1
    return alist

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)