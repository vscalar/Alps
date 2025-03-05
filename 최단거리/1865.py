import sys
from collections import defaultdict, deque
import heapq
input = sys.stdin.readline

TC = int(input())
edges = []
N, M, W = map(int, input().split())
for _ in range(M):
    edge = list(map(int, input().split()))
    edges.append(edge)

adjacency_list = defaultdict(list)
for index, (u, v, weight) in enumerate(edges): # construct adjacency_list
    adjacency_list[u].append((v, weight))
    adjacency_list[v].append((u, weight))

wormholes = []
for _ in range(W):
    u,v, w = map(int, input().split())
    wormhole = [u, v, -w]
    wormholes.append(wormhole)

for index, (u, v, weight) in enumerate(wormholes): # construct adjacency_list
    adjacency_list[u].append((v, weight))

distance = [float('inf')] * (N+1)
distance[1] = 0
for i in range(1, N+1):
    for neighbor, weight in adjacency_list[i]:
        distance[neighbor] = min(distance[neighbor], weight + distance[i])

print(distance)

