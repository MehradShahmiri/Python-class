compnun=50
s=int(input('guess a number: '))
d=1
while compnun!=s:
    if compnun<s:
        print('your guess is too high')
        s=int(input('guess a number: '))
    elif compnun>s:
        print('your guess is too low')
        s=int(input('guess a number: '))
    d=d+1
print('ywell done you took',d,'attempts')
