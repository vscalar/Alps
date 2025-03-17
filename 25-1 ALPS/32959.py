import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/32859

if __name__ == "__main__":
    #get N, M, S
    N, M = map(int, input().split())
    S = int(input())
    
    #record
    submission_timing = [10000] * (N+1)
    submission_log = [0] * (M+1)
    deposit_timing = [0] * (N+1)


    #get events
    for i in range(1,M+1):
        person, type = map(int, input().split()) #0: submit form, 1: deposit

        if type == 0:
            submission_log[i] = 1
            submission_timing[person] = i
        
        else:
            deposit_timing[person] = i
        
    #answer
    late_people = []

    for person in range(1, N+1):
        #not deposited
        if deposit_timing[person] == 0:
            continue
        
        #submitted beforehand
        if submission_timing[person] <= deposit_timing[person]:
            continue

        #not submitted but deposited
        deposit = deposit_timing[person]
        submission = submission_timing[person]
        if submission_timing[person] == 10000:
            if sum(submission_log[deposit:]) >= S:
                late_people.append(person)

        else:
            if sum(submission_log[deposit:submission]) >= S:
                late_people.append(person)


    #print answer
    if len(late_people) == 0:
        print(-1)
    else:
        for person in late_people:
            print(person)