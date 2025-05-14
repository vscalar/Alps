import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/9252

def get_lcs_length_and_subseq(str1, str2):
    #get lengthes
    length1 = len(str1)
    length2 = len(str2)
    def get_subseq(dp):
        i = length1
        j = length2
        ans = []
        cur_val = dp[i][j]
        while True:
            if i<=0 or j <=0:
                break
            up_val = dp[i-1][j]
            left_val = dp[i][j-1]
            if cur_val > up_val and cur_val > left_val:
                i -= 1
                j -= 1
                cur_val -= 1
                ans.append(str1[i])
            elif up_val >= left_val:
                i -= 1
            else:
                j -= 1
        ans.reverse()
        return ''.join(ans)


    dp = [[0]*(length2+1) for _ in range(length1+1)]
    for i in range(1, length1+1):
        for j in range(1, length2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    ans_len = dp[length1][length2]
    if ans_len == 0:
        return ans_len, None
    return ans_len, get_subseq(dp)

def main():
    #get two strings
    str1 = input().strip()
    str2 = input().strip()
    ans_len, subseq = get_lcs_length_and_subseq(str1, str2)
    print(ans_len)
    if subseq:
        print(subseq)

if __name__ == "__main__":
    main()

