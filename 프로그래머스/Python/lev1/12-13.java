//짝수와 홀수
//https://school.programmers.co.kr/learn/courses/30/lessons/12937?language=java
class Solution {
    public String solution(int num) {
        if (num%2 == 0)
            return "Even";
        return "Odd";
    }
}

//약수의 합
//https://school.programmers.co.kr/learn/courses/30/lessons/12928?language=java
class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i <= n; i++){
            if (n%i == 0){
                answer += i;
            }
        }
        return answer;
    }
}
    // if(시작값선언; 지속조건; 한번돈후 시행할 조건)

//평균 구하기
// https://school.programmers.co.kr/learn/courses/30/lessons/12944?language=java
class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        for(int i=0; i<arr.length; i++)
            answer += arr[i];
        answer = answer / arr.length;
        return answer;
    }
}

//자릿수 더하기
//https://school.programmers.co.kr/learn/courses/30/lessons/12931?language=java
import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;

        while (n != 0) {
            answer += n % 10;
            n /= 10;
        }
        return answer;
    }
}