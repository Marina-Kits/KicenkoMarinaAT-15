st=input()
res=""
for i in range(len(st)):
    if i==len(st)-1 or st[i+1]==" ":
        res+=st[i]
print(res)