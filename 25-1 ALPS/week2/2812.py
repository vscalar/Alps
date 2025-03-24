import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/2812

if __name__ == "__main__":
    # get N, K
    N, K = map(int, input().split())
    #get string
    string = input().strip()
    #count excluded nums
    count = 0
    stack = []
    #iterate through string
    for letter in string: 
        num = int(letter)        
        #pop the stack until it's empty or found larger num or removed K nums                                                   
        while stack and stack[-1] < num and count < K:  
            stack.pop()                                 
            count += 1
        stack.append(num)

    print(*stack[:N-K],sep='')