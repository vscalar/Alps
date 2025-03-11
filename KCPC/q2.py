import sys
input = sys.stdin.readline
import math
import heapq

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def dijkstra_2d(coords, start_index):
    # 좌표의 개수
    n = len(coords)
    
    # 시작점 설정 (다익스트라 알고리즘)
    distances = [float('inf')] * n
    distances[start_index] = 0
    pq = [(0, start_index)]  # (거리, 인덱스)

    while pq:
        logo_effect1 = 1
        current_dist, current_index = heapq.heappop(pq)
        if current_index == 0 or current_index == n-1:
            logo_effect1 = 0
            
        # 현재 점까지의 거리가 이미 더 짧으면 패스
        if current_dist > distances[current_index]:
            continue
        
        # 현재 점에서 다른 점으로의 거리 계산
        for i in range(n):
            logo_effect2 = 1
            if i == n-1:
                logo_effect2 = 0
                
            if i != current_index:
                dist = max(euclidean_distance(coords[current_index], coords[i])-logo_effect1-logo_effect2, 0)
                new_dist = current_dist + dist
                if new_dist < distances[i]:
                    distances[i] = new_dist
                    heapq.heappush(pq, (new_dist, i))

    return distances

if __name__ == "__main__":
    # get coordinates
    goal_coordinate = tuple(map(int, input().split()))
    num_logo = int(input())
    logo_list = [(0, 0)]
    for _ in range(num_logo):
        logo_coordinate = tuple(map(int, input().split()))
        logo_list.append(logo_coordinate)
    
    logo_list.append(goal_coordinate)
    #print(logo_list)
    
    #calculate distances
    start_index = 0
    dist = dijkstra_2d(logo_list, start_index)
    #print(dist)
    
    #return result
    print(dist[-1])