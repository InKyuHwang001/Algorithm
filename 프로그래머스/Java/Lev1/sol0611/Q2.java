package sol0611;

import static java.lang.Math.max;
import static java.lang.Math.min;

public class Q2 {
    public static long solution(int a, int b) {
        long answer = 0;
        for (int i = min(a, b); i <= max(a, b); i++) {
            answer += i;
        }
        return answer;
    }

    public static void main(String[] args) {
        int a = 5;
        int b = 3;
        System.out.println(solution(a, b));
    }
}
