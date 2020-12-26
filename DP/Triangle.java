import java.util.*;
class Triangle { 
    public int minimumTotal(List<List<Integer>> triangle) {
        int [][] dp = new int[triangle.size()][]; 
        for (int i = 0; i < triangle.size(); i++) { 
            dp[i] = new int[triangle.get(i).size()];
            Arrays.fill(dp[i], Integer.MAX_VALUE);
            //System.out.println(Arrays.toString(dp[i]));
        }
        dp[0][0] = triangle.get(0).get(0);
        System.out.println(dp[0][0]);
        for (int r = 1; r < triangle.size(); r++) { 
            for (int c = 0; c < triangle.get(r).size(); c++) { 
                for (int i = c - 1; i < c+1; i++) { 
                    if (i >= 0 && i < triangle.get(r-1).size()) {
                        //System.out.println(Integer.toString(r) + " " + Integer.toString(c));
                        dp[r][c] = Math.min(dp[r][c], dp[r-1][i]+triangle.get(r).get(c));
                        //System.out.println(Integer.toString(r) + " " + Integer.toString(c));
                    }
                }
            }
        }
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i <= dp[dp.length-1].length-1; i++) {
            ans = Math.min(ans, dp[dp.length-1][i]);
        }
        return ans;
    }
}