from itertools import product as pd
discountRate = [10,20,30,40]
def solution(users, emoticons):
    answer = []
    productsize = len(emoticons)
    #할인율 리스트 
    discounts = list(pd(discountRate, repeat = productsize))
    
    for dc in discounts:
        tmp = [0,0] #유저, 총액
        for mindc, tp in users:
            userspend = 0
            for idx, emoticon in enumerate(emoticons):
                if dc[idx] >= mindc:
                    userspend += emoticon*(1 - (dc[idx]/100))
            if userspend >= tp:
                tmp[0] += 1
            else:
                tmp[1] += userspend
            
        answer.append(tmp)
    answer.sort(key = lambda x: x[1])
    answer.sort(key = lambda x: x[0])
    
    return answer[-1]