def diff_letters(a,b):
    return sum ( a[i] != b[i] for i in range(len(a)) )

def isValidList(x):
    for i in range(0, len(x) - 1):
        if diff_letters(x[i],x[i+1]) != 1:
            return False
    return True

def stringsRearrangement(inputArray):

    import itertools

    x = list(itertools.permutations(inputArray))

    for spermutation in x :
        if(isValidList(spermutation)):
            return True
    return False



print(stringsRearrangement(["ab", "bb", "aa"]))



