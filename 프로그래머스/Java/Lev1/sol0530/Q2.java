package sol0530;

import java.util.stream.IntStream;

public class Q2 {
    public int solution(String s) {

        return Integer.parseInt(s);
    }

    public int solutionAdvanced(int n) {

        return IntStream
                .rangeClosed(1, n)
                .parallel()
                .filter(i -> n % i== 0)
                .sum();
    }
}
