def findParent(u):
    if parent[u] == u:
        return u

    parent[u] = findParent(parent[u])
    return parent[u]

def unionNode(u, v):
    u = findParent(u)
    v = findParent(v)
    if u != v: #if same node, then don't update
        parent[u] = v
        num[v] += num[u]

R, C = map(int, input().split())
parent = [i for i in range(R*C)]
num = [1 for i in range(R*C)]