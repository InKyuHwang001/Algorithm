package sol0612;

import java.util.stream.IntStream;

public class Q2 {


    public static int solution(int[] absolutes, boolean[] signs) {
        var ans = 0;
        for (int i = 0; i < absolutes.length; i++) {
            if (signs[i]) ans += absolutes[i];
            else ans -= absolutes[i];
        }

        return ans;
    }

    public static void main(String[] args) {
        int[] abs = {4, 7, 12};
        boolean[] signs = {true, false, true};
        System.out.println(solution(abs, signs));
    }
}
