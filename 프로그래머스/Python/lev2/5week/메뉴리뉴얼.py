from itertools import combinations
def solution(orders, course):
    set_menu = {}
    for i in course:
        for order in orders:
            for comb in combinations(order, i):
                comb = sorted(comb)
                comb = "".join(comb)
                if comb not in set_menu:
                    set_menu[comb] = 0
                set_menu[comb] += 1
                
    set_menu = {foods:cnt for foods, cnt in set_menu.items() if cnt > 1}
    set_menu = sorted(set_menu.items(), key = lambda x : (len(x[0]), -x[1]))
    
    len_menu_cnt = dict(zip(course, [-1] * len(course))) 
    
    answer = []
    for foods, cnt in set_menu:
        
        if len_menu_cnt[len(foods)] <= cnt:
            len_menu_cnt[len(foods)] = cnt
            answer.append(foods)
    return sorted(answer)