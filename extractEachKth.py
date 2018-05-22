
def extractEachKth(inputArray, k):
    nToRemove = int(len(inputArray)/k)
    final_arr = []
    prev = 0
    for i in range(0,nToRemove):
        posToRemove = int((i+1) * k) - 1
        final_arr += inputArray[prev:posToRemove]
        prev = posToRemove + 1
    final_arr += inputArray[prev:]
    return final_arr

#print(extractEachKth(([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),3))
def extractEachKth1(x, k):
    del x[k-1::k]
    return x


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("extractEachKth(([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),3)", setup="from __main__ import extractEachKth"))
    print(timeit.timeit("extractEachKth1(([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),3)", setup="from __main__ import extractEachKth1"))