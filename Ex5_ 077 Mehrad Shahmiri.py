print('Who do you whant to invite to the party')
q=input('1: ')
w=input('2: ')
e=input('3: ')
p=[q,w,e]
print(q)
o=input('type one of them')
print(p.index(o))
i=input('do you still wanthim or her come to the party yes/no')
if i=='no':
    p.remove(o)
    print(p)
