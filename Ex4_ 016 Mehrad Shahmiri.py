a=input('Is it rainy?')
b=a.lower()
if b!='yes':
    print('Enjoy your day')
else:
    s=input('Is it windy too?')
    d=s.lower()
    if d=='yes':
        print('It is too windy for an umbrella.')
    else:
        print('Take an umbrella')
