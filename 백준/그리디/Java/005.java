import java.util.*;

class Solution {
    public static void main(String[]args){

        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        int ans = 1; 

        while (b > a) {
            ans += 1;
            int tmp = b;
            
            if (b % 10 ==1) {
                b = b/10;
            } 
            else if (b%2 == 0){
                b = b/2;
            } 
        }

        if (a<b) {
            System.out.println(-1);
        } 
        else {
            System.out.println(ans);
        }

    }
}