import sys
input = sys.stdin.readline

#https://www.acmicpc.net/problem/32386

if __name__ == "__main__":
    #get N
    N = int(input())
    
    #dict to count tags
    tag_map = {}
    
    #get info of problems
    for _ in range(N):
        problem = input().split()   #data of a problem
        code = int(problem[0])      #code of a problem
        tag_num = int(problem[1])   #number of tags
        tags = problem[2:]          #list of tags
        
        #count tags in tag_map
        for tag in tags:
            if tag not in tag_map:
                tag_map[tag] = 0
            tag_map[tag] += 1
    
    #print(tag_map) #check tag_map
    
    #get max occurrence of tags
    max_count = max(tag_map.values())
    
    #get tags that occurred the most
    max_tags = [tag for tag, count in tag_map.items() if count == max_count]
    
    #if multiple tags in max_tags print -1 else print the tag
    if len(max_tags) > 1:
        print(-1)
    
    else:
        print(max_tags[0])