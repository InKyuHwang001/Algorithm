def solution(genres, plays):
    ans = []
    sgen = set(genres)
    #장르 
    dic1 = {}
    #장르별 노래
    dic2 = {}
    for gen in sgen:
        dic1[gen] = 0
        dic2[gen] = []
    for idx, (g, c) in enumerate(zip(genres, plays)):
        dic1[g] += c
        dic2[g].append([idx, c])
    
    #정렬한것 넣기
    for gen, tq in sorted(dic1.items(), key = lambda x: x[1], reverse = True):
        for idx, cnt in sorted(dic2[gen], key = lambda x: x[1], reverse = True)[:2]:
            ans.append(idx)

    return ans
"""
enumerate, zip

dic.items()
"""