def solution(today, terms, privacies):
    ans = []
    #오늘을 순수 날짜로
    yy, mm, dd = map(int, today.split("."))
    today = (yy * 12 + mm) * 28 + dd
    
    dicterms = {}
    for term in terms:
        ty, mm = term.split()
        dicterms[ty] = int(mm) * 28
    
    
    for idx, priv in enumerate(privacies):
        priday, ty = priv.split()
        py, pm, pd = map(int, priday.split('.'))
        pd = (py * 12 + pm) * 28 + pd 
        pd += dicterms[ty]
        if pd <= today:
            ans.append(idx+1)
    
    return ans