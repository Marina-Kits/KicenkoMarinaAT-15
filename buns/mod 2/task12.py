st=input()
res=""
el=" -()"
for i in range(len(st)):
    if not st[i] in el:
        res+=st[i]
print(res)
