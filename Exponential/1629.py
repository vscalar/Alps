import sys
input = sys.stdin.readline

def mod_pow(base, exp, mod):
    ret = 1
    base %= mod
    
    while exp > 0:
        if exp & 1:
            ret = ret * base %mod
        base = base*base%mod
        exp >>=1
    
    return ret
base, exp, mod= list(map(int, input().split()))
print(mod_pow(base, exp, mod))