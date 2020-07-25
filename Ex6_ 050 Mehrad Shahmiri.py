s=int(input('enter number betwenn 10 and 20: '))
while s<10 or s>20:
    if s<10:
        print('Too low')
        s=int(input('try again: '))
    else:
        print('Too high')
        s=int(input('try again: '))
print('Thank you')
