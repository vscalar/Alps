import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/11401
mod = 1000000007

def get_factorial_list(N):
    ans = [1, 1]
    for i in range(2, N+1):
        next = ans[-1] * i % mod
        ans.append(next)
    
    return ans

if __name__ == "__main__":
    #get N, K
    N, K = map(int, input().split())
    #get fact list
    fact = get_factorial_list(N)
    inv_fact = list(pow(x,mod-2,mod) for x in fact)
    print(fact[N]*inv_fact[N-K]*inv_fact[K]%mod)
