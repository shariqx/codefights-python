def boxBlur(image):
    tempOP = list()
    for i in range(0, len(image)):

        for j in range(0, len(image[i])):
            if i + 2 > len(image) or j + 2  > len(image[i]):
                continue
            else:
                y = [row[j:j+2] for row in image[i:i+2]]
                tempOP.append(y)
                j +=2
        i+=2
    return tempOP

x =boxBlur([[1, 2, 1],
              [2, 2, 2],
              [2, 2, 2],
              [1, 2, 3],
              [2, 2, 1]])