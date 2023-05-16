import java.util.*; 


class Pair{
    
    int next;
    int dist;
    
    public Pair(int next, int dist){
        this.next = next;
        this.dist = dist; 
    }

}

public class Main {
    
    public static int N, M;
    public static ArrayList<Pair>[] arr;
    public static boolean isVisited;
    public static boolean[] check; 
    public static StringBuilder sb = new StringBuilder();    
        
    public static void dfs(int curr, int end, int total){
        
        if(isVisited == true){
            return; 
        }
         
        if(isVisited == false && curr == end){
            isVisited = true;
            sb.append(total);
            sb.append('\n');
            return; 
        }     
           
        
        for(int i=0; i<arr[curr].size(); i++){
            int next = arr[curr].get(i).next;
            int dist = arr[curr].get(i).dist;               
        
            if(check[next] == false){
               check[next] = true; 
               dfs(next, end, total+ dist);
               check[next] = false; 
            }
        
       }
    }

    
    public static void main(String args[]) {
      
        Scanner sc = new Scanner(System.in); 
      
        N = sc.nextInt();
        M = sc.nextInt(); 
        arr = new ArrayList[N+10];
        check = new boolean[N+10];
        
        for(int i=1; i<=N; i++){
           arr[i] = new ArrayList<>(); 
        }
        
        for(int i=1; i<=N-1; i++){
           int a = sc.nextInt();
           int b = sc.nextInt();
           int dist = sc.nextInt(); 
           arr[a].add(new Pair(b, dist));
           arr[b].add(new Pair(a, dist)); 
        }
        
        
        for(int i=1; i<=M; i++){
            int start = sc.nextInt();
            int end = sc.nextInt();
            isVisited = false;
            check[start] = true; 
            dfs(start, end, 0);
            check[start] = false; 
        }
        
        
        System.out.println(sb.toString());

    }
}
