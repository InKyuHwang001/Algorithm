def solution(n, t, m, timetable):
    answer = 0
    
    timetable = [int(t[:2])*60 + int(t[3:]) for t in timetable]
    timetable.sort()
    
    bustime = [540 + t*i for i in range(n)]
    
    i = 0
    for bt in bustime:
        cnt = 0
        while cnt<m and i<len(timetable) and timetable[i]<=bt:
            i += 1
            cnt += 1
        if cnt<m:  
            answer = bt
        else:  
            answer = timetable[i-1]-1
    return str(answer//60).zfill(2) + ":" +str(answer%60).zfill(2)