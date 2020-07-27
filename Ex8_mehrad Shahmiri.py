def date(day,month,year):
    x=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year%4==0:
        if year%100==0:
            if year%400==0:
                x[1]=29       
        else:
            x[1]=29


    d=sum(x[:month-1])
    total=d+day
    return(total)

