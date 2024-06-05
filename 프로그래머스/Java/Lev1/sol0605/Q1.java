package sol0605;

class Q1 {
    public static boolean solution(int x) {

        String[] strings = String.valueOf(x).split("");
        int tmp = 0;

        for(String s: strings){
            tmp += Integer.parseInt(s);
        }

        return x % tmp == 0;
    }

    public static void main(String[] args){
        var n = 10;

        System.out.println(solution(n));
    }
}