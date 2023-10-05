st=input()
s=st[:st.index(",")]
i=st[-1]
j=0
while s[j]==i:
    j+=1
print(j)