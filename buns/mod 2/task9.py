st=input()
v="аеёиоуыэюя"
count1=0
count2=0
for i in range(len(st)):
    if st[i] in v:
        count1+=1
    elif st[i]!=" " and st[i]!="ъ" and st[i]!="ь":
        count2+=1
print(count1, count2)