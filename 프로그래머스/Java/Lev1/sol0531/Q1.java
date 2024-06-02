package sol0531;

import java.util.Arrays;
import java.util.stream.IntStream;
import java.util.stream.Stream;

class Q1 {
    public int solution(int n) {
        int answer = 0;

        String[] split = String.valueOf(n).split("");

        for (String s : split){
            answer += Integer.parseInt(s);
        }
        return answer;
    }

    public int solutionAdvance(int n) {
        int answer = 0;

        return Stream.of(String.valueOf(n).split(""))
                .mapToInt(Integer::parseInt)
                .sum();


    }
}