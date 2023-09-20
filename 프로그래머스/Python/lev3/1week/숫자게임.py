def solution(A, B):
    ans = 0
    A.sort(reverse = True)
    B.sort(reverse = True)
    for a in A:
        if a >= B[0]:
            continue
        ans += 1
        del B[0]
    return ans

"""
# continue vs pass
    continue의 경우: 하위 코딩을 건너뛰고 다음 순번의 loop를 수행
    pass의 경우    : 실행할 코드가 없는 것으로 다음 행동을 수행

        예시 
            # continue
                i = 0
                while i < 10:
                    i += 1 
                    if i % 2 == 0:   
                        continue      
                    print(i)  
                -----------------------
                (result)
                1
                3
                5
                7
                9

            # pass 
                i = 0
                while i < 10:
                    i += 1
                    if i % 2 == 0:    
                        pass        
                    print(i)    
                --------------------
                (result)
                1
                2
                3
                4
                5
                6
                7
                8
                9
                10

# del vs remove

    1. del : 인덱스로 삭제
    2. remove( ) 함수 : 값으로 삭제
"""