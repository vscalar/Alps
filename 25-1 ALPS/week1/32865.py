import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/32865

if __name__ == "__main__":
    #get N
    N = int(input())
    #get problem guesses
    guesses = [int(input()) for _ in range(N)]
    
    cur = 1 #0: fail, 1: success

    sum =  sum(guesses)
    if N -sum not in [0, 1]:  #if success - fail not 0 or 1 
        print(-1) #impossible
        exit()

    #use lists to track indices
    success_indices = [i for i in range(N) if guesses[i] == 0]
    fail_indices = [i for i in range(N) if guesses[i] > 0]
    ans = []

    #print(success_indices)
    #print(fail_indices)
    
    #iterate through guesses
    for i in range(N+sum):
        if cur == 1: #find success
            if success_indices: #if there exists success
                index = success_indices.pop() #remove last success index
                ans.append(index + 1)
            else:
                print(-1)
                exit()

            cur = 0 #find fail in the next loop

        else: #find fail
            if fail_indices:
                index = fail_indices[-1] #get last fail index
                guesses[index] -= 1
                ans.append(index + 1)
                if guesses[index] == 0:
                    fail_indices.pop()
                    success_indices.append(index)
            else:
                print(-1)
                exit()

            cur = 1
    
    for idx in ans:
        print(idx)