
# 100% pass solution
def passingCars(A):
    passing = 0
    zCount = 0
    for i in A:
        if i is 1:
            passing += zCount
        else:
            zCount += 1

    if passing > 1e9 or passing < 0:
        return -1
    else:
        return passing