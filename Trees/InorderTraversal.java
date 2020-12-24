/* *
 * Definition for a binary tree node.
 */

import java.util.*;

public class InorderTraversal {
    List<Integer> inorder;
    InorderTraversal() { 
        this.inorder = new ArrayList<Integer>();
    }
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
    public List<Integer> inorderTraversal(TreeNode root) {
        if (root != null) { 
            inorderTraversal(root.left);
            this.inorder.add(root.val);
            inorderTraversal(root.right);
        }
        return this.inorder;
    }
    public static void main(String[] args) {
        InorderTraversal s = new InorderTraversal();
        TreeNode root = s.buildTree(new Integer[]{ 1, null, 2, 3 });
        List<Integer> ans = s.inorderTraversal(root); 
        System.out.println(ans);
    }

}
