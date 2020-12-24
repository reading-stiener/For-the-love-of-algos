import java.util.*;
public class BuildTree { 
    public TreeNode buildTree(Integer[] arr) {
        TreeNode root = null;
        Queue<TreeNode> q = new LinkedList<>();
        int i = 0;
        TreeNode t = arr[i] == null ? null : new TreeNode(arr[i]);
        root = t;
        q.add(root);
        i++;
        while (!q.isEmpty() && i < arr.length) {
            TreeNode t1 = q.poll();
            if (t1 != null) {
                t1.left = arr[i] == null ? null : new TreeNode(arr[i]);
                q.add(t1.left);
                i++;
                if (i >= arr.length) {
                    break;
                }
                t1.right = arr[i] == null ? null : new TreeNode(arr[i]);
                q.add(t1.right);
                i++;
            }
        }
        return root;
    }
    public String printTree (TreeNode root) { 
        StringBuilder treeStr = new StringBuilder(); 
        Queue<TreeNode> q = new LinkedList<>(); 
        q.add(root);
        while (!q.isEmpty()) { 
            TreeNode curr = q.poll();
            treeStr.append((curr == null ? "null" : curr.val)).append(", ");
            if (curr != null) { 
                q.add(curr.left);
                q.add(curr.right);
            }
        }
        return treeStr.toString();
    }
}