def calculateGPA():
    number_courses=int(input('How many courses do you offer: '))
    score=input('Please enter your scores, separated by commas: ').split(',')
    score=[int(score) for score in score]
 
    GPA= sum(score)/number_courses 
    if GPA>=80 and GPA<=100:
        return 4.0
    elif GPA>=75 and GPA<=79:
        return 3.50
    elif GPA>=70 and GPA<=74:
        return 3.00
    elif GPA>=65 and GPA<=69:
        return 2.50
    elif GPA>=60 and GPA<=64:
        return 2.00
    elif GPA>=55 and GPA<=59:
        return 1.50
    elif GPA>=50 and GPA<=54:
        return 1.00
    elif GPA<50:
        return 0.00
   

def getHonours():
    gpa=calculateGPA()
    if gpa>=3.85 and gpa<=4.00:
        print('Summa Cum Laude')
    elif gpa>=3.70 and gpa<=3.84:
        print('Magna Cum Laude')
    elif gpa>=3.50 and gpa<=3.69:
        print('Cum Laude')
    else:
        print('No honours')

getHonours()