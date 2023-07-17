m=int(input('Enter a number: '))
num=1
print('MULTIPLICATION TABLE OF', m,'\n----------------------------')
while m>=0:
    if num>12:
        break
    answer=m*num
    print(m,'*', num, '=', answer )
    num+=1
