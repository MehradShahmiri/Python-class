def fib_list(r):
    s=[]
    if r<0: 
        print("Incorrect ") 
    elif r==1: 
        return s+[1]
    elif r==2: 
        return [1,1]
    else: 
        L = fib_list(r - 1)
        L.append(L[-2] + L[-1])
        return L
