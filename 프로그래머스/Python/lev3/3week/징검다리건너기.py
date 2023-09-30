#이분탐색
def solution(stones, k):
    answer = 0
    smin, smax = 0, max(stones)
    
    while smin<= smax:
        ct=0
        mid = (smin + smax) //2
        for s in stones:
            if (s-mid) <= 0:
                ct+=1
            else:
                ct = 0
            if ct>= k :
                break

        if ct < k:
            smin = mid + 1
        else:
            answer = mid
            smax = mid -1
            
    return answer