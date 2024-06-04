package sol0604;

class Q1 {

    private static final String ODD = "Odd";
    private static final String EVEN = "Even";

    private static String solution(int num) {

        if (num % 2 == 0) return EVEN;

        return ODD;
    }

    private static String solutionAdvance(int num) {

        return  (num % 2 == 0) ? EVEN : ODD;

    }

    public static void main(String[] args) {

        int n = 3;

        System.out.println(solution(n));
    }
}