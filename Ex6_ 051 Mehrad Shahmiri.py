p=int(input('choose a number: '))
print(p,' green bottles sitting on the wall',p,' green bottles sitting on the wall','And if one green bottle should accidentally fall,')

while p>0:
    d=int(input('How many green bottle will be hanging on the wall: '))
    while d!=p-1:
        d=int(input('No, try agian: '))
    print('There will be',d,'green bottle hanging on the wall')
    p=p-1
    print(p,' green bottles sitting on the wall',p,' green bottles sitting on the wall','And if one green bottle should accidentally fall,')
print(' there are no more green bottles hanging on the wall')
