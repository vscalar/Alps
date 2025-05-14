import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/2217

def get_max_weight(ropes: list[int]) -> int:
    # sort coins in descending order
    ropes_sorted = sorted(ropes, key=lambda x : -x)
    # initialize ans and cur_price
    ans = 0
    rope_count = 1
    for rope in ropes_sorted:
        cur_weight = rope * rope_count
        ans = max(cur_weight, ans)
        rope_count += 1

    return ans

def main():
    n = int(input())
    ropes = [int(input()) for _ in range(n)]
    print(get_max_weight(ropes))

if __name__ == "__main__":
    main()