st=input()[::-1]
st1=""
for i in range(len(st)):
    if st[i]==".":
        print(st1[::-1])
        st1=""
    else:
        st1+=st[i]
print(st1[::-1])