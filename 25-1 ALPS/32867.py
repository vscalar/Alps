import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/32861

if __name__ == "__main__":
    #get N, K
    N, K = map(int, input().split())

    #get piano keys
    piano_keys = list(map(int, input().split()))

    #record min key and max key
    min_key = piano_keys[0]
    max_key = piano_keys[0]

    #ans
    ans = 0

    #iterate through keys
    for i in range(1, N):
        cur_key = piano_keys[i]
        #update min max key
        min_key = min(min_key, cur_key)
        max_key = max(max_key, cur_key)
        #if difference of min key and max key is bigger than K
        if max_key - min_key >= K:
            ans += 1 #add ans
            min_key = max_key = cur_key
    
    #print ans
    print(ans)