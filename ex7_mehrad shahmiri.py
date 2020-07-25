def fib(r): 
    if r<0: 
        print("Incorrect ") 
    elif r==1: 
        return 0
    elif r==2: 
        return 1
    else: 
        return fib(r-1)+fib(r-2) 
  
