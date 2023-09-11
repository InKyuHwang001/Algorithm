def solution(today, terms, privacies):
    ans = []
    nterms = {}
    for term in terms:
        key, value = term.split()
        nterms[key] = int(value)
    today = list(map(int, today.split('.')))
    
    tmp = []
    for privacy in privacies:
        eday, term = privacy.split()
        ey, em, ed = map(int, eday.split('.'))
        em = em + nterms[term]
        ey += int((em - 1)//12)
        em = ((em-1)%12) + 1
        tmp.append([ey,em,ed])    
    for i in range(len(tmp)):
        if tmp[i][0] < today[0] or (tmp[i][0] == today[0] and tmp[i][1] < today[1]) or (tmp[i][0] == today[0] and tmp[i][1] == today[1] and tmp[i][2] <= today[2]):
            ans.append(i+1)

            
    return ans

## 시간으로 월년을 변환하기
def solution(today, terms, privacies):
    answer = []
    
    #오늘 날짜 변환
    ty, tm, td = map(int, today.split('.'))
    td += (ty*12 + tm) * 28
    
    # 기간 변환
    dterms = {}
    for term in terms:
        key, value = term.split()
        value = int(value) * 28
        dterms[key] = value
        
    #유효기간 만료일 변환
    eprivs = []
    for priv in privacies:
        eday, term = priv.split()
        ey, em, ed = map(int, eday.split('.'))
        ed += (ey*12 + em) * 28
        ed += dterms[term]
        eprivs.append(ed)

    for idx in range(len(eprivs)):
        if eprivs[idx] <= td:
            answer.append(idx+1)
    
    return answer