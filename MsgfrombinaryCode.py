def messageFromBinaryCode(code):
    x = 0
    out = ''
    while x +8  <= len(code):
        y = (x + 8)
        subst = code[x:y]
        #print(subst)
        theInt = int(subst,2)
       # print(theInt)
        asci = chr(theInt)
        out+=asci
        x = x+8
    return out

print(messageFromBinaryCode('010010000110010101101100011011000110111100100001'))