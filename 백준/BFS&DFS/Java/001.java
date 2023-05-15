import java.util.*;

// DFS
class Main {
    static boolean[][] arr;
    static boolean[] visited;
    static int n, m;
    static int cnt;

    private static void dfs(int idx) {
        cnt++;
        visited[idx] = true;
        for (int i = 1; i <= n; i++) {
            if (!visited[i] && arr[idx][i]) dfs(i);
        }
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();

        arr = new boolean[n+1][n+1];
        visited = new boolean[n+1];
        
        int x, y;
        for (int i = 0; i < m; i++) {
            x = sc.nextInt();
            y = sc.nextInt();
            arr[x][y] = arr[y][x] = true;
        }

        dfs(1);

        System.out.println(cnt - 1);
        sc.close();
    
    }

}

//BFS
class BFSMain{
    static boolean[][] arr;
    static boolean[] visited;
    static int n, m;
    static int cnt;
    static ArrayList<Integer> q;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();

        arr = new boolean[n+1][n+1];
        visited = new boolean[n+1];
        
        int x, y;
        for (int i = 0; i < m; i++) {
            x = sc.nextInt();
            y = sc.nextInt();
            arr[x][y] = arr[y][x] = true;
        }

        q =  new ArrayList<>();
        q.add(1);
        visited[1] = true;
        
        while (!q.isEmpty()){
            int idx = q.remove(0);
            for (int i = 1; i <= n; i++)
                if (!visited[i] && arr[idx][i]) {
                    cnt++;
                    visited[i] = true;
                    q.add(i);
                }
        }
        System.out.println(cnt);
        sc.close();
    }
}