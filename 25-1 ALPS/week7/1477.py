import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/1477

def main():
    n, m, l = map(int, input().split())
    # 0 for starting point and l for ending point
    locations = [0] + list(map(int, input().split())) + [l]
    locations.sort()
    start, end = 1, l-1
    res = 0
    while start<=end:
        count = 0
        mid = (start+end)//2
        for i in range(1, n+2):
            diff = locations[i]-locations[i-1]
            # divide until pieces are shorter than mid
            count += (diff-1)//mid
        # the minimum piece is longer than mid
        if count > m:
            start = mid+1
        else:
            end = mid-1
            res = mid
    print(res)

if __name__ == "__main__":
    main()