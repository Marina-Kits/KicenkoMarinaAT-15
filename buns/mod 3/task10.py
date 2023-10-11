matrix_size=int(input())
matrix1=[]
end_matrix=""
for i in range(0, matrix_size):
    matrix1.append([])
    for j in range(0, matrix_size):
        matrix1[i].append(j+1)
def matrix_output(a):
    for k in range(len(a)):
        for l in range(len(a)):
            if l<len(a)-1:
                end_matrix=", "
            else:
                end_matrix=""
            print(a[k][l], end=end_matrix)
        print()
def transp_matrix(a):
    b=[]
    for m in range(len(a)):
        b.append([])
        for n in range(len(a)):
            b[m].append(a[n][m])
    return b
matrix_output(matrix1)
print()
matrix_output(transp_matrix(matrix1))