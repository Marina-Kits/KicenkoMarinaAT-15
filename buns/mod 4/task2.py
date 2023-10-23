def power(a,n):
    if n%2==0:
        return power(a**2,n//2)
    if n==1:
        return a
    return a*power(a,n-1)
print(power(2,2))
print(power(2,3))
print(power(2,1))