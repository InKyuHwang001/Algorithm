def solution(s):
    answer = 0
    #i = 문자열의 시작 인덱스
    for i in range(len(s)):
    	#j = 문자열의 끝 인덱스
        for j in range(len(s), i, -1):
        	#i부터 j까지의 문자열 생성
            new_s = s[i:j]
            #뒤집었을 때에도 같으면 팰린드롬
            if new_s == new_s[::-1]:
            	#answer 값 갱신
                answer = max(answer, len(new_s))
    return answer