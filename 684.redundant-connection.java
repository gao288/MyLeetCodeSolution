import java.util.ArrayList;
import java.util.HashMap;
class Solution_684 {
    public int[] findRedundantConnection(int[][] edges){
        HashMap<Integer,ArrayList<Integer>> graph = new HashMap<Integer,ArrayList<Integer>>();
        int[] ret = new int[];
        for (int [] edge: edges){

            if(graph.containsKey(edge[1]) && dfs(graph,edge[0],edge[1])){
                ret = edge;
            }else{
                graph.computeIfAbsent(edge[0],k->new ArrayList<Integer>());
                if(!graph.containsValue(edge[1])) {
                    graph.get(edge[0]).add(edge[1]);
                }
                graph.computeIfAbsent(edge[1],k->new ArrayList<Integer>());
                if(!graph.containsValue(edge[0])) {
                    graph.get(edge[1]).add(edge[0]);
                }
            }


        }
        return ret;
    }
    public boolean dfs(HashMap<Integer,ArrayList<Integer>> graph, int target, int source){
        boolean ret = false;
        for(int edge: graph.get(source)){
            if(edge == target){
                return true;
            }else{
                ret = (ret | dfs(graph,target,edge));
            }

        }
        return ret;
    }
    public static void main(String [] args){
        Solution_684 S = new Solution_684();
        int[][] edges = {{1,2},{1,3},{2,3}};
        S.findRedundantConnection(edges);
    }
}



