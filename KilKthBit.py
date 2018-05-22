def killKthBit(n, k):
    return int(str(bin(n))[2:][:len(str(bin(n))) -2 - k] +'0'+ str(bin(n))[2:][k-1:],2)



print(killKthBit(37,4))