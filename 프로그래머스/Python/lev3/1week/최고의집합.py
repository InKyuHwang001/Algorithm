def solution(n, s):
    if n > s :
        return [-1]
    
    ans = []
    
    part = int(s//n)
    
    for _ in range(n):
        ans.append(part)
    elses = s%n
    
    for i in range(elses):
        ans[i] += 1
    ans.sort()
    
    return ans