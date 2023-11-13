from itertools import combinations as comb

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    combis = []
    for i in range(1, col+1):
        combis.extend(comb(range(col), i))
    #유일성
    uniqueness = []
    for com in combis:
        tmp = [tuple([item[x] for x in com])for item in relation]
        if row == len(set(tmp)):
            uniqueness.append(com)
    #최소성
    answer = set(uniqueness)
    for i in range(len(uniqueness)):
        for j in range(i+1, len(uniqueness)):
            if len(uniqueness[i]) == len(set(uniqueness[i]) & set(uniqueness[j])):
                answer.discard(uniqueness[j])
        
            
    return len(answer)