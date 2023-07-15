def compareStrings(garlands,flowers):
    count=0
    for i in flowers:
        if i in garlands:
            count+=1
    print(count)
#test
compareStrings('aA', 'aAAbbbb')
compareStrings('z','ZZ')