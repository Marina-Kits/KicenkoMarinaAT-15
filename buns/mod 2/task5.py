abc="abcdefghijklmnopqrstuvwxyz"
st=input()
i=st[0]
n=int(st[2:])
ind=(abc.index(i)+n) % 26
res=abc[ind]
print(res)
