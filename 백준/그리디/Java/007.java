
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
	public static int row;
	public static int col;
	public static int[][] A;
	public static int[][] B;
	public static int cnt;
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		row = sc.nextInt();
		col = sc.nextInt();
		A = new int [row][col];
		B = new int [row][col];

		//기본 map 세팅
		for(int i = 0 ; i <row; i ++) {
			String str = sc.next();
			for(int j = 0 ; j < col ; j++) 
				A[i][j] = Integer.parseInt(str.substring(j,j+1));
		}

		//바꾸고 싶은 map 세팅
		for(int i = 0 ; i <row; i ++) {
			String str = sc.next();
			for(int j = 0 ; j < col ; j++) 
				B[i][j] = Integer.parseInt(str.substring(j,j+1));
		}

		cnt = 0;
		for(int i = 0 ; i < row-2; i++) {
			for(int j = 0 ; j < col-2; j++) {
				if(A[i][j] != B[i][j]) {
					change(i,j);
					cnt++;
				}
			}
		}

		int flag = 0;
		for(int i = 0 ; i < row ; i++) {
			for(int j = 0 ; j < col ; j++) {
				if(A[i][j] == B[i][j])
					flag ++;
			}
		}

		if(flag == row*col)
			System.out.println(cnt);
		else 
			System.out.println(-1);

	}
	
	public static void change(int x , int y) {
		for(int i = x ; i <x+3 ; i++) {
			for(int j = y; j<y+3 ; j++) {
				A[i][j] = A[i][j] ^ 1 ;
			}
		}
	}


}