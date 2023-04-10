1.
//두 수의 곱
class Solution{
    public int Solution(int num1, int num2){
        int answ = 0;
        ans = num1 * num2;
        return ans
    }
}
2.
//숫자 비교하기
// https://school.programmers.co.kr/learn/courses/30/lessons/120807?language=java
class Solution {
    public int solution(int num1, int num2) {
        int ans = 0;
        if (num1 == num2)
            return 1;
        return -1;
    }
}
    //  한줄의 코드면 중괄호 생략 가능하지만 두줄 이상의 코드에서는 생략하면 원하는 결과를 얻기 힘들다.
3.
//두 수의 차
class Solution {
    public int solution(int num1, int num2) {
        int ans = num1 - num2;
        return ans;
    }
}
4.
//몫 구하기
class Solution {
    public int solution(int num1, int num2) {
        int answer = 0;
        answer = num1/num2;
        return answer;
    }
}
5.  
//나머지 구하기
class Solution {
    public int solution(int num1, int num2) {
        return num1%num2;
    }
}
6.
//나이 출력
class Solution {
    public int solution(int age) {
        int answer = 0;
        answer = 2023 - age;
        return answer;
    }
}
7.
//두수의 합
class Solution {
    public int solution(int num1, int num2) {
        int answer = 0;
        answer = num1 + num2;
        return answer;
    }
}
8.
//두 수의 나눗셈
class Solution {
    public int solution(int num1, int num2) {
        int answer = 0;
        answer = num1 * 1000 / num2;
        return answer;
    }
}
9.
//각도기
class Solution {
    public int solution(int angle) {
        if(angle < 90)
            return 1;
        else if (angle == 90)
            return 2;
        else if (angle < 180)
            return 3;
        else 
            return 4;
    }
}
10.
//짝수의 합
class Solution {
    public int solution(int n) {
        int ans = 0;
        for (int i = 1; i <= n ; i++){
            if (i%2 ==0)
                ans += i;
        }
        return ans;
    }
}