import sys
input = sys.stdin.readline

def matrixMultiply(A, B, mod):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])
    result = [[0 for j in range(cols_B)] for i in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] % mod
    return result

def mat_pow(base, exp, mod):
    size = len(base)
    ret = [[0 for j in range(size)] for i in range(size)]
    for i in range(size):
        ret[i][i] = 1
        
    while exp > 0:
        if exp & 1:
            result = matrixMultiply(ret, base, mod)
        base = matrixMultiply(base, base, mod)
        exp >>=1
        
    return result

N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
print(mat_pow(matrix , B, 1000))