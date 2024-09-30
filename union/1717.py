import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def findParent(u):
    if parent[u] == u:
        return u

    parent[u] = findParent(parent[u])
    return parent[u]

def unionNode(u, v):
    u = findParent(u)
    v = findParent(v)
    parent[u] = v

n, m = map(int, input().split())
parent = list(range(n+1))
computations = [list(map(int, input().split())) for _ in range(m)]

for sequence in computations:
    computationType, u, v = sequence
    if computationType == 0:
        unionNode(u, v)
    
    else:
        if findParent(u) == findParent(v):
            print("yes")
        
        else:
            print("no")