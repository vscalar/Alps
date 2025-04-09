import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/1920
def binary_search(space, target):
    low, high = 0, len(space) - 1
    while low <= high:
        mid = (low + high) // 2
        if space[mid] == target:
            return 1
        elif space[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return 0

if __name__ == "__main__":
    N = int(input())
    space = list(map(int, input().split()))
    space.sort()
    M = int(input())
    targets = list(map(int, input().split()))
    for target in targets:
        print(binary_search(space, target))
