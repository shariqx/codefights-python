
roads = [[1, 0], [1, 2], [8, 5], [9, 7],
         [5, 6], [5, 4], [4, 6], [6, 7]]





def cityConquering(n, roads):
    hmap = dict()
    for i in range(n):
        hmap[i]=set()
    for i in range(0, len(roads)):
        for j in range(1):
            from_node = roads[i][0]
            to_node = roads[i][1]
            hmap[from_node].add(to_node)
            hmap[to_node].add(from_node)


    out_arr = [-1] * (n)
    days_to_conquer = 1
    removed_keys = set()
    while True:
        all_are_empty = True
        this_removed = set()
        for key, value in hmap.items():
            hmap[key] = hmap[key] - removed_keys
        for key, value in hmap.items():
            if key in removed_keys:
                continue
            if len(value) == 1:
                removed_keys.add(key)
                this_removed.add(key)
                hmap[key] = set()
                all_are_empty = False

        if len(removed_keys) == 0:
            all_are_empty = True
        for i in this_removed:
            if(len(hmap[i]) > 0):
                hmap[hmap[i].pop()].remove(key)
            out_arr[i] = days_to_conquer
        if all_are_empty:
            break
        else:
            days_to_conquer += 1
    return out_arr


if __name__ == '__main__':
    print(cityConquering(10, roads))
