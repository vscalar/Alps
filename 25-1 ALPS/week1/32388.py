import sys
input = sys.stdin.readline
import math
import heapq

#https://www.acmicpc.net/problem/32388

#func that calculates euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

#dijkstra func
def dijkstra(coords, start_index):
    # num of coords
    n = len(coords)
    
    # initialize starting point
    distances = [float('inf')] * n
    distances[start_index] = 0
    pq = [(0, start_index)]  # (dist, index)

    while pq:
        #if current index is starting or ending point don't consider the logo
        logo_effect1 = 1
        current_dist, current_index = heapq.heappop(pq)
        if current_index == 0 or current_index == n-1:
            logo_effect1 = 0
            
        # ignore if longer
        if current_dist > distances[current_index]:
            continue
        
        # calculate dist
        for i in range(n):
            #check if i is the end point
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
    dist = dijkstra(logo_list, start_index)
    #print(dist)
    
    #return result
    print(dist[-1])