def almostIncreasingSequence(sequence):
    return  almostIncreasingSequenceHelper(sequence, 0)


def almostIncreasingSequenceHelper(sequence, count):
        if count > 1 :
            return False
        if len(sequence)  == 2:
            return sequence[0] > sequence[1]
        x = 0
        for x in range(0,len(sequence)-1):
                if sequence[x + 1]  < sequence[x]:
                    del(sequence[x])
                    if x - 1 == -1:
                        almostIncreasingSequenceHelper(sequence[0:len(sequence)], count + 1)
                    else:
                        almostIncreasingSequenceHelper(sequence[x-1:len(sequence)], count + 1)
        if x == len(sequence):
            return True

if __name__ =='__main__':
    x =  [1, 2, 1, 2]
    print(almostIncreasingSequence(x))