import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/10830

def square_matrix_mul(matrix1, matrix2, size, mod):
    ans = [[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                ans[i][j] += matrix1[i][k] * matrix2[k][j]
                ans[i][j] %= mod
    
    return ans

def square_matrix_pow(acc, base, size, power, mod):
    if power == 0:
        return acc
    if power % 2 == 1:
        new_acc = square_matrix_mul(acc, base, size, mod)
    else:
        new_acc = acc
    new_base = square_matrix_mul(base, base, size, mod)
    return square_matrix_pow(new_acc, new_base, size, power // 2, mod)

MOD = 1000

if __name__ == "__main__":
    N, B = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    identity = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    new_matrix = square_matrix_pow(identity, matrix, N, B, MOD)
    for line in new_matrix:
        print(' '.join(map(str, line)))
    