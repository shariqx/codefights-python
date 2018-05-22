adj =  [[False,True,True,False,False], 
 [True,False,True,False,False], 
 [True,True,False,True,True], 
 [False,False,True,False,True], 
 [False,False,True,True,False]]

def isButteFly(adj):
    counter = 0
    x = dict()
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            if adj[i][j]:
                counter+=1
               # adj[j][i] = False
                if i in x :
                    x[i] += 1
                else:
                    x[i] = 1
                if j in x :
                    x[j] += 1
                else: x[i] = 1
    sum = 0
    value_list = []
    for value in x.values():
        sum+=value
        value_list.append(value)
    if sorted(value_list)[:len(value_list) - 1] == [2,2,2,2] and value_list[-1] >= 4 and (counter == 6 and len(x) == 5):
        return True
    else: return False




print(isButteFly(adj))