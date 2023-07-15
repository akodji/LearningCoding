#this function takes a numerical score as a parameter, and returns the\
#corresponding letter grade and grade point
def calculateGPA(numerical_score):
    if numerical_score >= 85 and numerical_score <= 100:
        return (4.0, 'A+')
    elif numerical_score >= 80 and numerical_score < 85:
        return (4.0, 'A')
    elif numerical_score >= 75 and numerical_score <= 79:
        return (3.50, 'B+')
    elif numerical_score >= 70 and numerical_score <= 74:
        return (3.00, 'B')
    elif numerical_score >= 65 and numerical_score <= 69:
        return (2.50, 'C+')
    elif numerical_score >= 60 and numerical_score <= 64:
        return (2.00, 'C')
    elif numerical_score >= 55 and numerical_score <= 59:
        return (1.50, 'D+')
    elif numerical_score >= 50 and numerical_score <= 54:
        return (1.00, 'D')
    elif numerical_score < 50:
        return (0.00, 'E')

#this function takes a cumulative grade point average as a parameter and returns honour category 
def getHonours(take_CGPA):
    if take_CGPA>= 3.85 and take_CGPA <= 4.00:
        return'Summa Cum Laude'
    elif take_CGPA >= 3.70 and take_CGPA <= 3.84:
        return'Magna Cum Laude'
    elif take_CGPA >= 3.50 and take_CGPA <= 3.69:
        return 'Cum Laude'
    else:
        return 'None'

grades=[]
g_p=[]
mark=[]
a_plus = []
a_noplus=[]
b_noplus = []
b_plus = []
b_noplus = []
c_plus = []
c_noplus = []
d_plus = []
d_noplus = []
e_noplus = []

#this function allows user to enter the numerical grade they earned in a number of courses
def grade(num):
    for i in range(num):
        allofit=int(input('Please enter your score for one course and press enter: '))
        mark.append(allofit)
        grade=calculateGPA(allofit)
        grades.append(grade[1])
        g_p.append(grade[0])
        
        if grade[1] == 'A+':
            a_plus.append('1')
        elif grade[1] == 'A':
            a_noplus.append('1')
        elif grade[1] == 'B+':
            b_plus.append('1')
        elif grade[1] == 'B':
            b_noplus.append('1')
        elif grade[1] == 'C+':
            c_plus.append('1')
        elif grade[1] == 'C':
            c_noplus.append('1')
        elif grade[1] == 'D+':
            d_plus.append('1')
        elif grade[1] == 'E':
            e_noplus.append('1')
            
    for i in range(num):
        print('Mark:', mark[i], ',' 'Grade:', grades[i], ',', 'Grade point:', g_p[i])
    print('A+:', len(a_plus))
    print('A:', len(a_noplus))
    print('B+:', len(b_plus))
    print('B:', len(b_noplus))
    print('C+:', len(c_plus))
    print('C:', len(c_noplus))
    print('D+:', len(d_plus))
    print('D:', len(d_noplus))
    print('E:', len(e_noplus))
    
num=(int(input('How many courses would you like to enter information for: ')))
grade(num)


CGPA=sum(g_p)/len(g_p)
print('Your CGPA is', CGPA)
print('Honours:', getHonours(CGPA))    





