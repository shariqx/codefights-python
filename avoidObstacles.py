def avoidObstacles(inputArray):
    for i in range(2, 40):
        non_divisible = True
        for j in range(0, len(inputArray)) :
            if(int(inputArray[j]) % i == 0):
                non_divisible = False
                break
        if non_divisible:
            return i
print(avoidObstacles([2, 3]))