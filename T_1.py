def fast_pow(x,n):
    global c
    if (n<=1):
        return (1,x)[n]
    p=x
    a=x
    k=1
    while True:
        k2=k+k
        if k2<n:
            p=p*a
            c+=1
            a=p
            k=k2
        else:
            return p*fast_pow(x,n-k)
 
c=0
print(fast_pow(2,100))
print(c)