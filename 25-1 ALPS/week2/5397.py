import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/5397

if __name__ == "__main__":
    #get N
    N = int(input())
    #for loop
    for _ in range(N):
        #get input
        string = input().strip()
        #make ls, rs(left of cursor and right side of cursor)
        ls, rs = [], []
        #iterate through string
        for letter in string:
            if letter == "-":               #backspace
                if ls: ls.pop()             #if ls not empty, pop
            elif letter == "<":             #left arrow
                if ls: rs.append(ls.pop())  #move one element to rs
            elif letter == ">":             #right arrow
                if rs: ls.append(rs.pop())  #move one element to ls
            else:                           #alphabets
                ls.append(letter)
        
        ls.extend(reversed(rs)) 
        print(''.join(ls))
