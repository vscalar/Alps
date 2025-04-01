import sys
input = sys.stdin.readline
from collections import deque

#https://www.acmicpc.net/problem/1941

def is_connected(coords):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[True] *5 for _ in range(5)]
    #set coords to unvisited
    for x, y in coords:
        visited[x][y] = False
    #set queue
    queue = deque([(coords[0])])
    #visited coord of first student
    visited[coords[0][0]][coords[0][1]] = True
    length = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            #check if next_x and next_y are in range
            if next_x <0 or next_x>=5 or next_y <0 or next_y>=5:
                continue
            if not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                length += 1
                queue.append((next_x,next_y))
    #if not visited 7 students, return false
    return length == 7

def make_7(matrix, coords, start, s_num):
    ans = 0
    length = len(coords)
    if length == 7 and s_num >= 4:
        if is_connected(coords):
            return 1
    elif length ==7 and s_num < 4:
        return 0
    
    for i in range(start, 25):
        x = i // 5
        y = i % 5
        coords.append((x,y))
        ans += make_7(matrix, coords, i+1, s_num + (matrix[x][y] == 'S'))
        coords.pop()
    return ans

if __name__ == "__main__":
    #get matrix
    matrix = list(list(input()) for _ in range(5))
    #set ans
    ans = make_7(matrix, [], 0, 0)
    print(ans)
