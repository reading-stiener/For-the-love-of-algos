class FlattenBTtoLL {
    public void flatten(TreeNode root) {
        this.flattenRecur(root); 
    }
    public TreeNode flattenRecur(TreeNode root) {
        System.out.println(root);
        if (root == null) {
            return null;    
        } else if (root.left == null && root.right == null) { 
            return root;
        } else { 
            TreeNode leftTail = this.flattenRecur(root.left);
            TreeNode rightTail = this.flattenRecur(root.right);
            if (leftTail != null) { 
                leftTail.right = root.right;
                root.right = root.left;
                root.left = null; 
            }
            return (rightTail == null) ? leftTail : rightTail;
        }
    }
    public static void main(String[] args) { 
        BuildTree tree = new BuildTree();
        TreeNode root = tree.buildTree(new Integer[] {1,2,5,3,4,null,6});
        FlattenBTtoLL test = new FlattenBTtoLL();
        test.flatten(root);
        System.out.println(tree.printTree(root));
    } 
}