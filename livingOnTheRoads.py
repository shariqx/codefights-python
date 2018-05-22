
def getConnectedCities(city_arr):
    out = []
    for idx, boolean in enumerate(city_arr):
        if boolean:
            out.append(idx)
    return out

def livingOnTheRoads(roadRegister):
    city_num = -1
    city_dict = {}

    iniesta = [] # iniesta's last classico 07/05/2018, Gracias Maestro :')
    for i in range(0, len(roadRegister)):
        x = list()
        x.extend(getConnectedCities(roadRegister[i]))
        if len(x) == 0 :
            continue
        for y in x:
            city_name = str(i)+'_'+str(y)
            iniesta.append(city_name)
            city_num += 1
            city_dict[city_name] = city_num
            roadRegister[y][i] = False
    out_arr = [[False for x in range(len(iniesta))] for x in range(len(iniesta))]

    for i in range(len(iniesta)):
        curr_city = iniesta[i]
        for j in range(i + 1, len(iniesta)):
            curcity_arr = curr_city.split('_')
            nextcity_arr = iniesta[j].split('_')

            if curcity_arr[0] in nextcity_arr or curcity_arr[1]  in nextcity_arr:
                out_arr[city_dict[curr_city]][city_dict[iniesta[j]]] = True
                out_arr[city_dict[iniesta[j]]][city_dict[curr_city]] = True
    print(out_arr)
    print(city_dict)
    return out_arr

if __name__ == '__main__':
     roadRegister = [[False,True,True,True],
     [True,False,False,True],
     [True,False,False,True],
     [True,True,True,False]]

     print(livingOnTheRoads(roadRegister))
