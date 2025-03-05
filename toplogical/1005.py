import sys
from collections import defaultdict, deque
input = sys.stdin.readline


def topological_sort_kahn(graph):
    # Compute in-degree (number of incoming edges for each node)
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Initialize a queue with nodes having in-degree of 0
    queue = deque([node for node in graph if in_degree[node] == 0])

    # List to store the topological sort result
    result = []

    # Process nodes in the queue
    while queue:
        node = queue.popleft()
        result.append(node)

        # Decrease the in-degree of neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            distances[neighbor] = max(distances[neighbor], distances[node] + times[neighbor])
            #print(node, neighbor)
            #print(distances)

            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    # If result contains all nodes, it is a valid topological sort
    if len(result) == len(graph):
        return result
    else:
        # Cycle detected (graph is not a DAG)
        raise ValueError("Graph contains a cycle, topological sort not possible.")
    
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    distances = list(times)
    #print(distances)
    graph = dict()
    for i in range(1,N+1):
        graph[i] = []
        
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        
    #print(graph)
        
    target = int(input())
    topological_sort_kahn(graph)
    #print(distances)
    print(distances[target])