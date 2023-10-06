def solution(n, m, x, y, r, c, k):
    answer = ''
    #불가능한경우
    dis = abs(x-r) + abs(y-c)
    if dis > k :
        return "impossible"
    elif (k - dis)% 2 == 1:
        return "impossible"
    #가능한 경우
    down = max(0,r - x)
    left = max(0, y - c)
    up = max(0, x - r)
    right = max(0,c - y)
    pair = (k - dis)/2
    
    for _ in range(k):
        if (down or pair)  and x < n:
            answer += 'd'
            if down:
                down -= 1
            else:
                pair -= 1
                up += 1
            x += 1
        elif (left or pair)  and y > 1:
            answer += 'l'
            if left:
                left -= 1
            else:
                pair -= 1
                right += 1
            y -= 1
        elif (right or pair)  and y < m :
            answer += 'r'
            if right:
                right -= 1
            else:
                pair -= 1
                left += 1
            y += 1
        else: 
            answer += 'u'
            if up:
                up -= 1
            else:
                pair -= 1
                down += 1
            x -= 1
    return answer