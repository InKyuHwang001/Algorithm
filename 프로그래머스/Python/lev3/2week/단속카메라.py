"""
새로운 숫자를 키로 하여 계산하기
"""
def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    key = -30_001
    
    for route in routes:
        s, e = route
        if s > key:
            answer += 1
            key = e
            
    return answer