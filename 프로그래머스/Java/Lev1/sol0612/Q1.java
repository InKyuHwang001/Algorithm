package sol0612;

class Q1 {
    private static final String KIM = "Kim";

    public static String solution(String[] seoul) {

        for(int i = 0; i < seoul.length; i++){
            if (seoul[i].equals(KIM)){
                return "김서방은 "+ i +"에 있다";
            }
        }
        return "김서방 없다요";
    }

    public static void main(String[] args){
        String[] n = {"Jane", "Kim"};

        System.out.println(solution(n));
    }
}