/**
 * 나머지가 1이 되는 수 찾기
 * 
 * https://school.programmers.co.kr/learn/courses/30/lessons/87389?language=java
 * 정답: O
 * 난이도: 하
 */

//내 풀이 
class Solution {
    public int solution(int n) {
        int ans = 1;
        while (ans < n) {
            if(n % ans == 1){
                return ans;
            } else {
                ans += 1;
            }
        }
        return ans;
    }
}

// 참고 품이
class Solution {
    public int solution(int n) {
        int answer = 1;

        while(n % answer != 1){
            answer++;
        }
        return answer;
    }
}
/**
 * x만큼 간격이 있는 n개의 숫자
 * 
 * https://school.programmers.co.kr/learn/courses/30/lessons/12954
 * 정답: O
 * 난이도: 하
 */

//내 풀이 
class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        long num = x;
        for(int i = 0; i < answer.length; i++){
            answer[i] = num;
            num += x;
        }
        return answer;
    }
}

//참고 풀이
//import java.util.*;
class Solution {
    public static long[] solution(int x, int n) {
        long[] answer = new long[n];
        answer[0] = x;

        for (int i = 1; i < n; i++) {
            answer[i] = answer[i - 1] + x;
        }

        return answer;

    }
}