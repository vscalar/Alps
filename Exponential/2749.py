import sys
input = sys.stdin.readline

def mul_mat(a, b):
    x = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % 1000000
    y = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % 1000000
    z = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % 1000000
    w = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % 1000000

    return [[x, y], [z, w]]

def matrixMultiply(A, B, mod):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])
    result = [[0 for j in range(cols_B)] for \
        i in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] % mod
    return result

def mat_pow(base, exp, mod):
    size = len(base)
    ret = [[0 for j in range(size)] for \
        i in range(size)]
    
    for i in range(size):
        ret[i][i] = 1
        
    while exp > 0:
        if exp & 1:
            result = matrixMultiply(ret, base, mod)
        base = matrixMultiply(base, base, mod)
        exp >>=1
        
    return result

N = int(input()) -1
base = [[1,1], 
        [1,0]]
B = [[1, 0], 
     [0, 1]]

while N>0:
    if N%2 == 1:
        B = mul_mat(base, B)
    base = mul_mat(base, base)
    N>>=1

print(B[0][0])
