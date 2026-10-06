str1, str2 = 'uff', 'bee'

flag = True

if len(str1) != len(str2):
    flag = False
else:
    map1, map2 = {}, {}
    for i in range(len(str1)):
        if (str1[i] in map1) and (map1[str1[i]] != str2[i]):
            flag = False
            break
        else:
            map1[str1[i]] = str2[i]
        if (str2[i] in map2) and (map2[str2[i]] != str1[i]):
            flag = False
            break
        else:
            map2[str2[i]] = str1[i]
print(map1, map2)

# Print result
if flag:
    print('Isomorphic String')
else:
    print('Not a Isomorphic String')

