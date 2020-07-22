sal= int(input('sal miladi vared konid:'))
if sal%4==0:
    if sal%100==0:
        if sal%400==0:
            print('Leap year')
        else:
            print('Normal year')
    else:
        print('Leap year')
else:
    print('Normal year')
print('Done')
