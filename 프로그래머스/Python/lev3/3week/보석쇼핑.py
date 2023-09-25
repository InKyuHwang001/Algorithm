def solution(gems):
    ans = [0, len(gems)]
    size = len(set(gems))
    lgem = len(gems)
    s, e = 0, 0
    dic = {gems[0]: 1}
    
    while s < lgem and e < lgem:
        if len(dic) == size:
            if e - s < ans[1] - ans[0]:
                ans = [s, e]
            else:
                dic[gems[s]] -= 1
                if dic[gems[s]] == 0:
                    del dic[gems[s]]
                s += 1
        else:
            e += 1
            if lgem <= e:
                break
            if gems[e] in dic:
                dic[gems[e]] += 1
            else:
                dic[gems[e]] = 1
                
    return [x + 1 for x in ans]