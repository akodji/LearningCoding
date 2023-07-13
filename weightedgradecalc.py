#asks user for grades
hw_g=int(input('Please enter your homework grade: '))
exam_g=int(input('Please enter your exam grade: '))
dis_g=int(input('Please enter your discussion grade: '))

#weights
hweight=0.4
eweight=0.5
dweight=0.1
add_weight=0.4+0.5+0.1


total=(hw_g*hweight)+(exam_g*eweight)+(dis_g*dweight)/add_weight
print(total)

