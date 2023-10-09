def solution(id_list, report, k):
    answer = [0] * (len(id_list))
    report = list(set(report))
    #신고 받은 수
    dicid = {x:[] for x in id_list}
    for re in report:
        a, b = re.split()
        dicid[b].append(a)
    #신고로 받을 돈 계산
    for key, peoples in dicid.items():
        size = len(peoples)
        if size >= k:
            for pe in peoples:
                answer[id_list.index(pe)]+= 1
    return answer