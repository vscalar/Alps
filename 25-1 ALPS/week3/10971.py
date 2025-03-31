import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

#https://www.acmicpc.net/problem/10971
def hamilton(matrix, N, to_visit, cur_city):
    #set ans to maximum
    ans = float('inf')
    #no more to_visit then go to starting point
    if not to_visit:
        if matrix[cur_city][0] == 0:
            return float('inf')
        else:
            return matrix[cur_city][0]
        
    for i in range(len(to_visit)):
        next_city = to_visit[i]
        #if there's a path cur_city to next_city
        if matrix[cur_city][next_city] != 0:
            new_to_visit = to_visit[:i] + to_visit[i+1:]
            #compare current path and path to next_city
            ans = min(ans, matrix[cur_city][next_city] + hamilton(matrix, N, new_to_visit, next_city))
    return ans

if __name__ == "__main__":
    #get N
    N = int(input())
    #set visited list
    visited = []
    #get graph
    matrix = dict()
    for i in range(N):
        matrix[i] = list(map(int, input().split()))
    to_visit = list(range(1,N))
    
    print(hamilton(matrix,N,to_visit,0))
