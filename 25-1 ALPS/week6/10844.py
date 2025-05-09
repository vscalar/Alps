import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/10844

MOD = 1000000000
def get_num_of_stair_nums(digits:int)-> int:
    dp = [[0]* 10 for _ in range(digits)]
    dp[0] = [0] + [1] * 9
    for i in range(digits-1):
        dp[i+1][0] = dp[i][1]
        dp[i+1][9] = dp[i][8]
        for j in range(1, 9):
            dp[i+1][j] = (dp[i][j-1] + dp[i][j+1])%MOD
    
    return sum(dp[-1])%MOD

if __name__ == "__main__":
    n = int(input())
    print(get_num_of_stair_nums(n))
