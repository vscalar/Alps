import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/1126

def get_min_inner_product(length:int, list1: list[int], list2: list[int]) -> int:
    # sort list1 in ascending order
    list1_sorted = sorted(list1, key=lambda x : x)
    # sort list2 in descending order
    list2_sorted = sorted(list2, key=lambda x : -x)
    # initialize ans and cur_price
    ans = 0
    for i in range(length):
        ans += list1_sorted[i] * list2_sorted[i]

    return ans

def main():
    length = int(input())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    print(get_min_inner_product(length, list1, list2))

if __name__ == "__main__":
    main()