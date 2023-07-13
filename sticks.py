stick1 = int(input('Please enter the length of your first stick: '))
stick2 = int(input('Please enter the length of your second stick: '))
stick3 = int(input('Please enter the length of your third stick: '))
def is_triangle(stick1, stick2, stick3 ):
    if (stick3>=stick1+stick2) or (stick2 >=stick1+stick3) or (stick1>=stick2+stick3) :
       print(False)
    else:
       print(True)

def can_triangle():
    if is_triangle(stick1,stick2, stick3):
        print('Can form a triangle')
    else:
        print('Cannot form a triangle')
can_triangle()
