def arrayMaxConsecutiveSum(inputArray, k):
    max1 = sum(inputArray[:k])
    prev_sum = sum(inputArray[:k])

    if len(inputArray) < 1:
        return inputArray[0]
    if(len(inputArray) == k):
        return max1
    if k == 1 :
        return max(inputArray)
    for x in range(1, len(inputArray)) :
        if(x + (k-1) == len(inputArray)):
            break
        if prev_sum - inputArray[x-1] + inputArray[x + k-1] > max1:
            max1 = abs(prev_sum -inputArray[x-1] + inputArray[x + k-1])
        prev_sum = prev_sum - inputArray[x-1] + inputArray[x + k-1]
    return max1


a= [1,2,3,4,5,6]

print(arrayMaxConsecutiveSum(a,2))