def topological_sort_dfs(graph):
    visited = set()
    result = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(neighbor)
        result.append(node)  # Add node after visiting all neighbors

    # Perform DFS on each node in the graph
    for node in graph:
        if node not in visited:
            dfs(node)

    # Reverse the result list to get the correct topological order
    return result[::-1]

import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
def makeGraph():
    ans = dict()
    for i in range(1,N+1):
        ans[i] = []
    for _ in range(M):
        a, b = map(int, input().split())
        ans[a].append(b)

    return ans
        
graph = makeGraph()
ans = topological_sort_dfs(graph)

#print(graph)
print(*ans)