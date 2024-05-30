public class Sol0530 {
    public static void main(String[] args) {

//        Q01.solution("123");
//        Q01.solutionAdvance("1234");
//
//        Q02.solution("1234");
        System.out.println((Q03.solution(12)));
    }
}

class Q01 {

    static boolean solution(String s) {
        int count = 0;
        var array = s.toLowerCase().split("");

        for (int i = 0; i < array.length; i++) {
            if ("p".equals(array[i])) {
                count++;
            } else if ("y".equals(array[i])) {
                count--;
            }
        }
        if (count == 0) {
            return true;
        }
        return false;
    }

    static boolean solutionAdvance(String s) {
        s = s.toUpperCase();

        return s.chars().filter(e -> 'P' == e).count() == s.chars().filter(e -> 'Y' == e).count();
    }
}

class Q02 {

    public static int solution(String s) {

        return Integer.parseInt(s);
    }
}

class Q03 {

    public static int solution(int n) {
        int answer = 0;

        for (int i = 1; i <= n; i++){
            if ( n%i== 0){
                answer += i;
            }
        }

        return answer;
    }
}