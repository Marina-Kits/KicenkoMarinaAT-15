N=int(open("input.txt").readline())
x = 0
y = 0
length=1
step=-1
distance_to_corner=0
x_y="x"
for i in range(N):
    if x_y=="x":
        if distance_to_corner==length:
            distance_to_corner=0
            x_y="y"
            y+=step
        else:
            x+=step
    else:
        if distance_to_corner==length:
            distance_to_corner=0
            step*=-1
            length+=1
            x_y="x"
            x+=step
        else:
            y+=step
    distance_to_corner+=1
open("output.txt","w").write(str(x)+" "+str(y))