package sol0602;

public class Q2 {

    public static long solution(long n) {
        double sqrt = Math.sqrt(n);
        if (sqrt % 1 == 0) {
            return (long) Math.pow(sqrt + 1, 2);
        } else return -1;
    }

    public static void main(String[] args) {
        long n = 3L;

        System.out.println(solution(n));
    }
}
