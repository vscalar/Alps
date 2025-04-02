import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/1629

def mod_pow(base, exp, mod):
    ret = 1
    base %= mod
    
    while exp > 0:
        # odd num, then multiply
        if exp & 1:
            ret = ret * base % mod
        # square base
        base = base*base%mod
        #shift right exp(exp//=2)
        exp >>=1
    
    return ret
base, exp, mod= list(map(int, input().split()))
print(mod_pow(base, exp, mod))