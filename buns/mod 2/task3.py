st=input()
a=int(st[:st.index(' ')])
b=int(st[st.index(' ')+1:st.rindex(' ')])
c=int(st[st.rindex(' ')+1:])
res=(a+b+c)-max(a,b,c)-min(a,b,c)
print(res)