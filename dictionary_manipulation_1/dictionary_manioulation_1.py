import copy
a = {"0": [1,2,3,4], "1": [1,2], "2": [1,5], "3": [3,7,8], "4": [2,3,5]}
b = {"0": [3], "1": [4], "2": [2,4], "3": [3,4], "4": [1]}
a = b
output = {"0": [1,2,3,4], "2": [1,5], "3": [3,7,8]}
temp = copy.deepcopy(a)
to_remove = []
for each in temp:
    remove = True
    for each_element in temp[each]:
        found = False
        for each1 in temp:
            if each != each1 and each1 not in to_remove:
                if each_element in temp[each1]:
                    found = True
                    break
        if found == False:
            remove = False
            break
    if remove:
        to_remove.append(each)
print(to_remove)
for each in to_remove:
    del a[each]
print(a)
        
