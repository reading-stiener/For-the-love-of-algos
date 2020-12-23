import java.util.*;

class CombinationSum {
    
 
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        int n = candidates.length;
        List<List<Integer>> combs = new ArrayList<List<Integer>>();
        ArrayList<Integer> comb = new ArrayList<Integer>();
        this.combinations(candidates, target, 0, n, comb, combs);
        return combs;
    }
    public void combinations(int[] candidates, int target, int idx, int n, List<Integer> comb, List<List<Integer>> combs){ 
        System.out.println(comb);
        //System.out.println(target);
        if (target == 0) { 
            //System.out.println(comb);
            ArrayList<Integer> newList = new ArrayList<Integer>(comb);
            combs.add(newList);
        } else if (target < 0) { 
            //System.out.println("STOP");
            return;
        } 
        for (int i = idx; i < n; ++i) {
            comb.add(candidates[i]);
            this.combinations(candidates, target-candidates[i], i, n, comb, combs);
            comb.remove(comb.size()-1);

        }           
    }

    public static void main(String[] args) { 
        CombinationSum s = new CombinationSum();
        System.out.println(s.combinationSum(new int[] {2,3,7}, 7));
    }
}