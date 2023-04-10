/**
 * 짝수와 홀수
 * 
 * https://school.programmers.co.kr/learn/courses/30/lessons/12937
 * 정답: O
 * 난이도: 극하
 */

//내 풀이 
class Solution {
    public String solution(int num) {
        
        if (num % 2 == 0) {
            return "Even";
        } else {
            return "Odd";
        }
    }
}

// 참고 풀이
class Solution {
    public String solution(int num){
        return (num % 2 == 0) ? "Even" : "Odd";
    }
}

/**
 * 평균 구하기
 * 
 * https://school.programmers.co.kr/learn/courses/30/lessons/12944
 * 정답: O
 * 난이도: 하 
 */

 // 내 풀이
 class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        
        for (double num : arr) {
            answer += num;
        }
        
        return answer / arr.length;
    }
}

// 참고 풀이

// import java.util.*;
// import java.lang.*;
class Solution {
    public double solution(int[] arr) {

        return Arrays.stream(arr).average().getAsDouble();
    }
}

/**
 * Java 8부터는 컬렉션을 처리하는데 유용한 기능인 스트림(Stream)이 추가
 *  중간 연산: 스트림 요소를 변환하거나, 걸러내거나, 정렬하는 등의 작업을 수행
 *  최종 연산: 스트림을 닫고 결과를 도출
 * 
 *  이점
 *  1. 코드가 간결해짐
 *  2. 병렬처리
 *  3. 지연연산 지원
 * 
 * map(): 요소를 다른 요소로 변환합니다.
 * filter(): 조건에 맞는 요소만 걸러냅니다.
 * sorted(): 요소를 정렬합니다.
 * distinct(): 중복 요소를 제거합니다.
 * forEach(): 요소를 하나씩 처리합니다.
 * reduce(): 요소를 하나씩 줄여가며 연산을 수행합니다.
 * collect(): 요소를 수집하여 다른 자료구조에 저장합니다.
 */