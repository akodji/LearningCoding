def compareStrings(garlands,flowers):
    if len(garlands)>=1 and len(flowers)<=50:
        print('Great!')
    else:
        print('Length requirement has not been met') 
        
        
    count=0
    for i in flowers:
        if i in garlands:
            count+=1
    print(count)
#test
compareStrings('aA', 'aAAbbbb')
compareStrings('z','ZZ')
