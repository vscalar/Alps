import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/14888
def backtraking(index, operator_num, acc):
    min_ans, max_ans = float('inf'), -float('inf')
    #if reached the end, return (acc, acc)
    if index == N:
        return acc, acc
    #iterate through 4 operators
    for i in range(4):
        if not operator_num[i]:
            continue
        if i == 0:
            next_acc = acc + seq[index]
        elif i == 1:
            next_acc = acc - seq[index]
        elif i == 2:
            next_acc = acc * seq[index]
        elif i == 3 and acc <0:
            next_acc = -(-acc // seq[index])
        else:
            next_acc = acc // seq[index]
            
        operator_num[i] -= 1
        next_min, next_max = backtraking(index+1,operator_num, next_acc)
        operator_num[i] += 1
        min_ans = min(min_ans, next_min)
        max_ans = max(max_ans, next_max)
    return min_ans, max_ans

if __name__ == "__main__":
    #get N
    N = int(input())
    #get seq
    seq = list(map(int, input().split()))
    #get num of operators
    operator_num = list(map(int, input().split()))
    #get min_ans, max_ans
    min_ans, max_ans = backtraking(1, operator_num, seq[0])
    print(max_ans)
    print(min_ans)