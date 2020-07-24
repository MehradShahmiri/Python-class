s=[111,222,333,444]
print(*s, sep='\n')
d=int(input('inter 3 digit number: '))
if d==s[0] or d==s[1] or d==s[2]:
    print(s.index(d)+1)
else:
    print('That is not in the list')
