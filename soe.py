n = int(input())
mat = [True for _ in range(n +1)]
mat[0] = False
mat[1] = False

for i in  range(2,n):
    for j in range(i*i, n+1 , i):
        mat[j] = False

for n,i in enumerate(mat):
    print(n, i) 
