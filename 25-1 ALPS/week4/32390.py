import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/32390
mod = 1000000007

def get_factorial_list(N):
    ans = [1, 1]
    for i in range(2, N+1):
        next = ans[-1] * i % mod
        ans.append(next)
    
    return ans

if __name__ == "__main__":
    #get N, K
    N, M = map(int, input().split())
    #get target num
    targets = list(map(int, input().split()))
    #get fact list
    fact = get_factorial_list(N)
    inv_fact = list(pow(x,mod-2,mod) for x in fact)
    ans = pow(2, N-M) * fact[N] % mod
    for i in range(M):
        ans = ans * inv_fact[targets[i]] %mod
    print(ans)

