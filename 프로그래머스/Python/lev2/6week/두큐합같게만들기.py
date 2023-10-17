from collections import deque
def solution(queue1, queue2):
    answer = 0
    sq1 = sum(queue1)
    sq2 = sum(queue2)
    st = sq1 + sq2
    limit = 2*(len(queue1) + len(queue2))
    q1, q2 = deque(queue1), deque(queue2)
    if st % 2 != 0:
        return -1
    cnt = 0
    while True:
        if sq1 >sq2:
            tmp = q1.popleft()
            q2.append(tmp)
            sq1 -= tmp 
            sq2 += tmp
            cnt += 1
        elif sq1 <sq2:
            tmp = q2.popleft()
            q1.append(tmp)
            sq2 -= tmp 
            sq1 += tmp
            cnt += 1
        else:
            return cnt
        if cnt > limit:
            return -1