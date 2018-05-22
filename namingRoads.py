

if __name__ == '__main__':
    roads =  [[5,1,3],
 [0,2,0],
 [2,4,2],
 [4,3,1],
 [8,5,5],
 [4,3,4]]
    ls = list()
    nodes = set()
    x = dict()
    roads_list = list()
    for i in range(0, len(roads)):
            if roads[i][2] in x:
                x[roads[i][2]].add(roads[i][1])
                x[roads[i][2]].add(roads[i][0])
            else:
                x[roads[i][2]] = set()
                roads_list.append(roads[i][2])
                x[roads[i][2]].add(roads[i][1])
                x[roads[i][2]].add(roads[i][0])
    print(x)
    roads_list = sorted(roads_list)
    for i in range(0, len(roads_list) - 1):
        one = set(x.get(roads_list[i]))
        two = set(x.get(roads_list[i + 1]))
        three = set(one.intersection(two))
        if len(three) > 0:
            print('false')
    print('true')





