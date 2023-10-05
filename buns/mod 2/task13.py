st=input()
s0=0
s1=0
for i in range(1,len(st)+1):
    if i%2==0:
        s0+=int(st[i-1])
    else:
        s1+=int(st[i-1])
if (s1+3*s0)%10==0:
    print("yes")
else:
    print("no")