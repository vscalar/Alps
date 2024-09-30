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
    if u != v: #if same node, then don't update
        parent[u] = v
        num[v] += num[u]

testCase = int(input())

for _ in range(testCase):
    peopleNum = int(input())
    parent = [i for i in range(2*peopleNum)]
    num = [1 for i in range(2*peopleNum)]
    d = dict()
    idx = 0
    
    for _ in range(peopleNum):
        person1, person2 = input().split()
        try:
            tmp = d[person1]
        
        except:
            d[person1] = idx
            idx += 1
        
        try:
            tmp = d[person2]
        
        except:
            d[person2] = idx
            idx += 1
            
        unionNode(d[person1], d[person2])
        print(num[findParent(d[person1])])
        
        