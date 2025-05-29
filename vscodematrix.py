



M = [[2,1],[1,3]]
b = [[3],[-1]]
Mb = [] 

nrows = 2
ncols = 2
for i in range(0, nrows):
    sum = 0
    for j in range(0, ncols):
        sum = sum + M[i][j] * b[j][0]
    Mb.append(sum)

print(Mb)