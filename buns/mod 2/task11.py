st=input()
res=False
for i in range(len(st)):
    for j in range(len(st)):
        if i!=j and st[i]==st[j] and st[i]!=" ":
            res=True
            break
print(res)