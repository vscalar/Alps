import sys
from collections import defaultdict, deque
import heapq
input = sys.stdin.readline

def dijkstra(start): # run dijkstra and return distance list
    distance = [float('inf')] * (V+1)
    distance[start] = 0
    to_visit = [(0, start)] # (distance, node)
    while to_visit:
        #print(distance)
        cur_dist, cur_node = heapq.heappop(to_visit)

        if cur_dist > distance[cur_node]: # no need to use longer distance
            continue
        
        # Explore neighbors
        for neighbor, weight in adjacency_list[cur_node]:
            new_dist = cur_dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(to_visit, (new_dist, neighbor)) # only consider shortened neighbor

    return distance[1:]

V, E = map(int, input().split())
start = int(input())
edges = []
for _ in range(E):
    edge = list(map(int, input().split()))
    edges.append(edge)

adjacency_list = defaultdict(list)
for index, (u, v, weight) in enumerate(edges): # construct adjacency_list
    adjacency_list[u].append((v, weight))

distance_list = dijkstra(start)
for dist in distance_list:
    print(dist if dist != float('inf') else "INF")