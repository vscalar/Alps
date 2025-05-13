import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/17404

# color is selected for the first house
def get_min_cost_given_color(length:int, color:int, matrix):
    dp = [[float('inf')]*3 for _ in range(length)]
    dp[0][color] = matrix[0][color]
    for i in range(3):
        dp[1][i] = dp[0][color] + matrix[1][i]
        # set cost of choosing the same color in a row as inf
        if i == color:
            dp[1][i] = float('inf')
    
    for i in range(2, length):
        dp[i][0] = matrix[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = matrix[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = matrix[i][2] + min(dp[i-1][0], dp[i-1][1])
    
    # set cost of choosing the same color in a row as inf
    dp[length-1][color] = float('inf')
    return min(dp[length-1])

def main():
    length = int(input())
    matrix = [tuple(map(int, input().split())) for _ in range(length)]
    # initialize ans
    ans = float('inf')
    for color in range(3):
        ans = min(ans, get_min_cost_given_color(length, color, matrix))
    print(ans)

if __name__ == "__main__":
    main()