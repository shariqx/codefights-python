import numpy as np

roads = [[False,False],
 [False,False]]

def getConnectedCities(city_arr):
    out = []
    for idx, boolean in enumerate(city_arr):
        if boolean:
            out.append(idx)
    return out


def removeCitites(arr,cities):
    for i in cities:
        arr[cities]

"""
[[False,True,True,False,True],
 [True,False,False,True,True],
 [True,False,False,False,False],
 [False,True,False,False,False],
 [True,True,False,False,False]]
"""

if __name__ == '__main__':

    num_of_cities = len(roads)
    i = 0
    np_roads = np.array(roads)
    while i < num_of_cities:
        if i + 1 < len(np_roads) and np_roads[i][i+1] :
            conn_cities = getConnectedCities(np_roads[i+1])
            conn_cities.remove(i)
            for x in conn_cities:
                    np_roads[i][x] = True
                    np_roads[x][i] = True
            np_roads[i][i+1] = False
            np_roads = np.delete(np_roads,i+1,0)
            np_roads = np.delete(np_roads,i + 1,1)
            i += 1
        else:
            i += 2

    print(np_roads.tolist())


#def merge(city1, city2):

