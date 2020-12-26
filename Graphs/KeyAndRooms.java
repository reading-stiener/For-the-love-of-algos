import java.util.HashSet;
import java.util.Queue;
import java.util.Set;
import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.LinkedList;
class KeyAndRooms {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Set <Integer> visited = new HashSet<>();
        Queue<Integer> q = new LinkedList<>();
        q.add(0);
        // Implemening BFS on graph
        while (!q.isEmpty()) { 
            Integer room = q.poll();
            //System.out.println(room);
            visited.add(room);
            for (int i=0; i < rooms.get(room).size(); i++) { 
                if (!visited.contains(rooms.get(room).get(i))) { 
                    q.add(rooms.get(room).get(i));
                } 
            } 
        }
        //System.out.println(visited);
        if (visited.size() == rooms.size()) { 
            return true;
        } else {
            return false;
        }
    }
    public static void main(String[] args) {
        KeyAndRooms s =  new KeyAndRooms();
        ArrayList<List<Integer>> test =  new ArrayList<List<Integer>>();
        test.add(Arrays.asList(1,3));
        test.add(Arrays.asList(3,0,1));
        test.add(Arrays.asList(2));
        test.add(Arrays.asList(0));
        System.out.println(s.canVisitAllRooms(test));
    }
}