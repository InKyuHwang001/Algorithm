def solution(n, times):
    answer = 0
    l, r = 0, max(times) * n
    while l <= r:
        m = (l + r) // 2
        tmp = 0
        for time in times:
            tmp += m // time
        if tmp >= n:
            answer = m
            r = m - 1
        else:
            l = m + 1
    return answer 