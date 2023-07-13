P=10000
n=12
r=8/100
t=float(input('Please enter the time in years: '))


final_amount=P*(1+r/n)**(n*t)
print(final_amount)
