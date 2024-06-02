package sol0530;

class Q1 {

    boolean solution(String s) {
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

    boolean solutionAdvance(String s) {
        s = s.toUpperCase();

        return s.chars().filter(e -> 'P' == e).count() == s.chars().filter(e -> 'Y' == e).count();
    }
}