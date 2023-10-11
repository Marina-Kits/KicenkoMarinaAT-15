st = input()
l = []
while st != "":
    l.append([])
    for i in st:
        l[-1].append(i)
    st = input()
win = ""
for i in range(len(l)):
    g=True
    for j in range(len(l)-1):
        if l[i][j]!=l[i][j+1]:
            g=False
            break
    if g:
        win=l[i][0]
for i in range(len(l)):
    v=True
    for j in range(len(l)-1):
        if l[j][i]!=l[j+1][i]:
            v=False
            break
    if v:
        win=l[0][i]
d=True
for i in range(len(l)-1):
    if l[i][i]!=l[i+1][i+1]:
        d=False
        break
if d:
    win=l[0][0]
d=True
for i in range(len(l)-1):
    if l[i][-1-i]!=l[-1-i][i]:
        d=False
        break
if d:
    win=l[0][-1]
if win=="":
    print("Ничья")
else:
    print(win)