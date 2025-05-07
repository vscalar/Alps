import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/1932

def get_value_of_pos(matrix, position: tuple[int, int])->int:
    
    x, y = position
    if x+1>=n:
        return matrix[x][y]
    
    if dp[x][y] !=0:
        return dp[x][y]
    
    dp[x][y] = matrix[x][y] + max(get_value_of_pos(matrix, (x+1, y)), get_value_of_pos(matrix, (x+1, y+1)))
    return dp[x][y]

#get n
n = int(input())

# get triangle and dp
matrix = [list(map(int, input().split()))+ [0]*(n-i-1) for i in range(n)]
dp = [[0] * n for _ in range(n)]

for x in range(n-1, -1, -1):
    for y in range(x+1):
        dp[x][y] = get_value_of_pos(matrix, (x, y))

print(dp[0][0])


