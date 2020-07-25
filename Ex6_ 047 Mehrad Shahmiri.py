a=int(input('enter a number: '))
b=int(input('enter another number: '))
t= a=b
s=input('Do you want to add another number?')
while s=="y":
    c=int(input('enter a number: '))
    s=input('Do you want to add another number?')
    t=t+c
print('total=',t)
