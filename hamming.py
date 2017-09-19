def distance(x,y):
    c=0
    z=len(x)
    if len(x)!=len(y):
        raise ValueError
    else:
        for i in range(0,z):
            if(x[i]!=y[i]):
                c=c+1
        return c
