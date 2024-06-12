package sol0611;

import java.util.stream.IntStream;

class Q1 {
    public static int solution(int n) {
        for (int i = 1; i < n; i++) {
            if (n%i == 1){
                return i;
            }
        }
        return 0;
    }

    public static int solutionAdvance(int n) {
        return IntStream.range(2, n).filter(i -> n % i == 1).findFirst().orElse(0);
    }

    public static void main(String[] args){
        int n = 10;

        System.out.println(solution(n));
        System.out.println(solutionAdvance(n));
    }
}