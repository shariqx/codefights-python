def fileNaming(names):
    main_dict = dict()
    out = list()
    for name in names:
        (x,a) = recrusiveNameSearch(main_dict,name)
        main_dict = x
        out.append(a)
    return out

def recrusiveNameSearch(dic, name):
    ret = name
    new_name = name
    while True:
        if new_name in dic:
            new_name = name + '('+ str(dic[name] + 1) +')'
            dic[name] = dic[name] + 1
        else:
            break
    dic[new_name] = 0
    return (dic,new_name)

print(fileNaming(["doc", "doc", "image", "doc(1)", "doc"]))