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

N = int(input())
M = int(input())
parent = list(range(N))
adjacent = [list(map(int, input().split())) for _ in range(N)]

course = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if adjacent[i][j] == 1:
            unionNode(i, j)

pivotCity = course[0] - 1
for city in course:
    if findParent(pivotCity) != findParent(city-1):
        print('NO')
        exit(0)

print("YES")
    