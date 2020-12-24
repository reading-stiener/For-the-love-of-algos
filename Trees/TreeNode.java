class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    public TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
    public String toString() { 
        if (this.val == 0)  {
            return "null";
        } else {
            return Integer.toString(this.val);
        }
    }
}