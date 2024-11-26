def AddDict(dic1, dic2):
    newdic = {}
    for key in dic1:
        if key in dic2:
            newdic[key] = dic1[key] + dic2[key]
        else:
            newdic[key] = dic1[key]
    
    for key in dic2:
        if key not in dic1:
            newdic[key] = dic2[key]
    return newdic

dict1 = {'a':10, 'b':20, 'c':30}
dict2 = {'a':12, 'b':34, 'd':60}

print(AddDict(dict1, dict2))


