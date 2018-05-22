def isLucky(n):
    first = 0
    second = 0
    half = len(str(n)) / 2
    cnt = 0
    while(n > 0):
        if cnt < half:
            first += n % 10
        else:
            second += n % 10
        n = int(n / 10)
        cnt +=1

    return first == second

print(isLucky(127254))