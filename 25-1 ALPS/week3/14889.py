import sys
input = sys.stdin.readline
from itertools import combinations

#https://www.acmicpc.net/problem/14889

def get_team_power(team:tuple, matrix) -> int:
    #set ans
    ans = 0
    length = len(team)
    #iterate 
    for i in range(length):
        for j in range(i+1, length):
            p1 = team[i]
            p2 = team[j]
            ans += matrix[p1][p2]+matrix[p2][p1]
    return ans

def get_min_diff(N, matrix):
    ans = float('inf')
    #make combinations
    combinations_list = list(combinations(range(N), N//2))
    #make list of team power
    team_power_list = [get_team_power(team,matrix) for team in combinations_list]
    length = len(team_power_list)
    #calculate difference
    for i in range(length//2):
        ans = min(ans, abs(team_power_list[i] - team_power_list[length-1-i]))
    return ans
    
if __name__ == "__main__":
    #get N
    N = int(input())
    #get matrix
    matrix = list(list(map(int, input().split())) for _ in range(N))
    #get ans
    ans = get_min_diff(N, matrix)
    print(ans)