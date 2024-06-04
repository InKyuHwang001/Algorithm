package sol0604;

import java.util.Arrays;

public class Q2 {
    public static double solution(int[] arr) {
        var tmp = 0.0d;
        for(double i : arr) tmp += i;

        return tmp / arr.length;
    }

    public static double solutionAdvance(int[] arr) {
        return Arrays.stream(arr).average().orElse(0);
    }

    public static void main(String[] args){
        int[] n = {1, 2, 3, 4};

        System.out.println(solution(n));
    }
}
