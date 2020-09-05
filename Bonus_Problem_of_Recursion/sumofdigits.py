def fun(n):
    if n==0:
        return 0
    small=n%10
    c=small+fun(n//10)
    if c>9:
        return fun(c)
    else:
        return c
n=11*9999991
print(fun(n+11155))