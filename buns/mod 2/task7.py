st=input()
n0=0
n1=0
for i in range(len(st)):
    if st[i]=="0":
        n0+=1
    else:
        n1+=1
if n0==n1:
    print("yes")
else:
    print("no")