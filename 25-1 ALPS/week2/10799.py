import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/10799

if __name__ == "__main__":

    #get input
    ps = input().strip()

    #make a stack
    stack = []
    #ans
    ans = 0
    for p in ps:
        if stack == []:
            prev_p = "("
            stack.append(p)
            continue
        
        if p == "(":
            stack.append(p)
            prev_p = "("
        elif p == ")" and prev_p == "(": #laser
            prev_p = ")"
            stack.pop()
            ans += len(stack)
        elif p == ")" and prev_p == ")": #end of rod
            prev_p = ")"
            stack.pop()
            ans += 1
        else:
            pass
    
    print(ans)
