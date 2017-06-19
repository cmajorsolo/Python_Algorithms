def bubbleSort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(0, i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    return list

L = [1,19,10,14,15]
print(bubbleSort(L))