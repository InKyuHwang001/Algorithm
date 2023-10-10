import math
 
def time_fun(t, in_out):
    o = list(t.split(':'))
    t = int(o[0])* 60 + int(o[1])
    if in_out == 'IN':
        t = t*(-1)
    return t
 
def solution(fees, records):
    answer = []
    cars = []
    note = {}
    for i in range(len(records)):
        cars.append(list(records[i].split()))
        note[cars[i][1]]=cars[i][0]
    note = sorted(note.items(), key=lambda item: item[0])
    for i in note:
        time = 0
        count = 0
        for j in range(len(cars)):
            if cars[j][1] == i[0]:
                time += time_fun(cars[j][0], cars[j][2])
                count +=1
        if count%2:
            time += time_fun('23:59', 'OUT')
        if time>fees[0]:
            fee = fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]
        else:
            fee = fees[1]
        answer.append(fee)
    return answer