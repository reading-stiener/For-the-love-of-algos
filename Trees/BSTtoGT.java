class BSTtoGT {
    public TreeNode bstToGst(TreeNode root) {
        this.bstToGT(root, null);
        return root;
    }
    public int bstToGT(TreeNode root, TreeNode parent) {
        if (root != null) { 
            int rightChildVal = this.bstToGT(root.right, parent);
            if (parent != null && root.right == null) { 
                root.val += parent.val + rightChildVal;
            } else { 
                root.val += rightChildVal;
            }
            this.bstToGT(root.left, root);
            TreeNode temp = root;
            while (temp.left != null) { 
                temp = temp.left;
            }
            return temp.val;
        } else {
            return 0;
        }
    }
}