/**
 * 자릿수 더하기
 * 
 * https://school.programmers.co.kr/learn/courses/30/lessons/12931
 * 정답: O
 * 난이도: 하
 */

//내 풀이 
public class Solution {
    public int solution(int n) {
        int ans = 0;

        while(n > 0){
            ans += n%10;
            n/=10;
        }
        
        return ans;
    }
}

// 참고 풀이
public class Solution {
    public int solution(int n) {
        int answer = 0;
        String s = Integer.toString(n); 
        
        for(int i=0; i<s.length(); i++){
            answer += Integer.parseInt(s.substring(i, i+1));
        }
        return answer;
    }
}

/**
 * 약수의 합
 * 
 * https://school.programmers.co.kr/learn/courses/30/lessons/12928
 * 정답: O
 * 난이도: 하 
 */

 // 내 풀이
 class Solution {
    public int solution(int n) {
        int ans = 0;
        for (int i = 1; i <= n; i++){
            if (n%i == 0) {
                ans += i;
            }
        }
        return ans;
    }
}