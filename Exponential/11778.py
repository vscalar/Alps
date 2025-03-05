import sys
input = sys.stdin.readline

def mul_mat(a, b):
    x = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % 1000000007
    y = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % 1000000007
    z = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % 1000000007
    w = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % 1000000007

    return [[x, y], [z, w]]


N, M = map(int, input().split())
N -= 1
M -= 1
def getFibo(num):
    base = [[1,1], 
            [1,0]]
    B = [[1, 0], 
        [0, 1]]

    while num>0:
        if num%2 == 1:
            B = mul_mat(base, B)
        base = mul_mat(base, base)
        num>>=1

    return B[0][0]

def factorize(n):
    ret = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
        ret.add(i)
    if n > 1:
        ret.append(n)

    return ret

def phi(n):
    ret = n
    for p in factorize(n):
        ret = ret // p * (p-1)
    
    return ret

fibo1, fibo2 = getFibo(N), getFibo(M)

