L=['friends','braking bad','prison brake','westworld']
print(*L, sep='\n')
p=input('enter another show')
q=int(input('position'))-1
L.insert(q,p)
print(L)
