import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/1931

def get_max_schedule(length: int, appointments: list[tuple[int, int]]) -> int:
    # sort appointments according to the time it finishes
    appointments_sorted = sorted(appointments, key = lambda x : (x[1], x[0]))
    #initialize ans
    ans = 0
    cur_time = 0
    for start, finish in appointments_sorted:
        # can schedule the appointment
        if start >= cur_time:
            ans += 1
            cur_time = finish
    
    return ans

def main():
    length = int(input())
    appointments = [tuple(map(int, input().split())) for _ in range(length)]
    print(get_max_schedule(length, appointments))

if __name__ == "__main__":
    main()