import math
def boxBlur(image):
    op = list()
    for i in range(0, len(image)):
        tempOP = list()
        for j in range(0, len(image[i])):
            if i + 3 > len(image) or j + 3 > len(image[i]):
                continue
            else:
                tempOP.append(findAvg([row[j:j+3] for row in image[i:i+3]]))
                j +=3
        if len(tempOP) > 0:
            op.append(tempOP)
        i+=3
    return op



def findAvg(image):
    sum  =  0
    for i in range(0, len(image)):
        for j in range(0, 3):
            sum += image[i][j]
    return int(sum/9)

print(boxBlur([[208,99,59,136,161,6,219,192,85,49],
 [194,105,43,254,153,225,171,197,1,154],
 [221,178,119,169,134,7,76,61,99,22],
 [161,254,172,12,174,200,216,107,109,109]]))